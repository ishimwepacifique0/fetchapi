from django.db import models

# Create your models here.

class Data(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    phonenumber = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.name
