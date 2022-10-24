from rest_framework import serializers
from .models import *

class Fetchserialiser(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['id','name','age','phonenumber','email']