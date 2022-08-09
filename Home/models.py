from asyncio import streams
from statistics import mode
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    regno = models.CharField(max_length=20)
    standard = models.IntegerField()
    section = models.CharField(max_length=1)
    stream = models.CharField(max_length=15)
    password = models.CharField(max_length=20)

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    teacherid = models.CharField(max_length=20)
    contact = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    classestaught = models.CharField(max_length=500)
    password = models.CharField(max_length=20)
