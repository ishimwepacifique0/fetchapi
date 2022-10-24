from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *

# Create your views here.
class API(GenericAPIView):
    serializer_class = Fetchserialiser
    def get(self,request):
        alldata = Data.objects.all()
        serializer = Fetchserialiser(alldata,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        # data = JSONParser().parse(request)
        serializer = Fetchserialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return JsonResponse(serializer.errors,status=400)

class Apidata(GenericAPIView):
    def get(self,request,id):
        selectone = Data.objects.get(id=id)
        serializer = Fetchserialiser(selectone)
        return Response(serializer.data)

    def put(self,request,id):
        selectone = Data.objects.get(id=id)
        serializer = Fetchserialiser(selectone,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self,request,id):
        selectone = Data.objects.get(id=id)
        selectone.delete()
        return HttpResponse(status=201)


