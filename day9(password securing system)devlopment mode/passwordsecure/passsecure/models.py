from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class usertable(models.Model):
    userid=models.IntegerField(primary_key=True, default=1)
    username=models.CharField(max_length=25)
    userpass=models.CharField(max_length=30)

class secure(models.Model):
    id=models.IntegerField(primary_key=True)
    platform=models.CharField(max_length=25)
    accname=models.CharField(max_length=30)
    accpassword=models.CharField(max_length=11)
    userid=models.IntegerField(models.ForeignKey(usertable,default=1, verbose_name=(""), on_delete=models.CASCADE)) 
    date=models.DateField()


def __str__(self):
    return self.name

