from django.db import models

# Create your models here.
class users(models.Model):
    username=models.CharField(max_length=50,unique=True)
    email=models.CharField(max_length=50,unique=True)
    password=models.CharField(max_length=255)
    phone=models.CharField(max_length=20)
    country=models.CharField(max_length=50)
    language=models.CharField(max_length=50)

