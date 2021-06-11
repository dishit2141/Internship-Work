from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.CharField(max_length=30)
    phone=models.CharField(max_length=11)
    msg=models.TextField()
    date=models.DateField()

def __str__(self):
    return self.name
