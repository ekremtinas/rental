from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class iha_marka(models.Model):
    marka_adi=models.CharField(max_length=50,unique=True)


class iha_model(models.Model):
    model_adi=models.CharField(max_length=50,unique=True)
    marka_id=models.ForeignKey(iha_marka, on_delete=models.CASCADE)

class iha_kategori(models.Model):
    kategori_adi=models.CharField(max_length=50,unique=True)
    

class iha(models.Model):
    iha_adi=models.CharField(max_length=50,unique=True)
    agirlik=models.FloatField()
    saatlik_fiyati=models.FloatField()
    resim=models.CharField(max_length=500)
    model_id=models.ForeignKey(iha_model, on_delete=models.CASCADE)
    kategori_id=models.ForeignKey(iha_kategori, on_delete=models.CASCADE)

class kiralama(models.Model):
    iha_id=models.ForeignKey(iha, on_delete=models.CASCADE)
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    kiralama_baslangic = models.DateTimeField()
    kiralama_bitis = models.DateTimeField()
    kiralama_ucret = models.FloatField()
