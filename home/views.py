from django.shortcuts import render
from .admin import iha,iha_kategori,iha_marka,iha_model,kiralama
from django.db import connection
from django.http import HttpResponse
from django.core import serializers
from datetime import timedelta
from datetime import datetime
from django.contrib.auth.models import User
# Create your views here.
def home(request):

    drones=[]
    if request.method=="POST":
        category=request.POST["category"]
        brand=request.POST["brand"]
        model=request.POST["model"]
        max_hour_pay=request.POST["max-hour-pay"]

        if category=="" and brand=="" and model=="" and max_hour_pay=="" :
            drones= iha.objects.all()
        else:
            if category!="":
                drones= iha.objects.filter(kategori_id=category)
            if brand!="":
                drones=iha.objects.filter(model_id__marka_id=brand)
            if  model!="":
                drones= iha.objects.filter(model_id=model)
            if max_hour_pay!="":
                drones=iha.objects.filter(saatlik_fiyati__lte=max_hour_pay)
      

       
    else:
        drones= iha.objects.all()
    
    categories= iha_kategori.objects.all()
    brands= iha_marka.objects.all()
    models= iha_model.objects.all()
    return render(request,"index.html",{
        "drones":drones,
        "categories":categories,
        "brands":brands,
        "models":models
    })
def my_rentals(request):

    rentals= kiralama.objects.all()
    return render(request,"my-rentals.html",{
        "rentals":rentals,
    })



def models_by_brand(request, brand_id):
    models=iha_model.objects.filter(marka_id=brand_id)
    data = serializers.serialize('json', models)
    return HttpResponse(data, content_type="application/json")

def rental(request):
    if request.method=="POST":
        iha_id=request.POST["iha_id"]
        user_id=request.POST["user_id"]
        startdate=request.POST["startdate"]
        enddate=request.POST["enddate"]
        # iha ve kullanıcı nesnelerini önce tanımlamanız gerekiyor
        iha_id=int(iha_id)
        user_id=int(user_id)
        ihaObject = iha.objects.get(id=iha_id)
        userObject = User.objects.get(id=user_id)
        enddate = datetime.strptime(enddate, '%Y-%m-%dT%H:%M')
        startdate = datetime.strptime(startdate, '%Y-%m-%dT%H:%M')
        # kiralama süresini hesaplayın
        kiralama_suresi = enddate - startdate
        kiralama_saatleri = kiralama_suresi / timedelta(hours=1)

        # kiralama ücretini hesaplayın
        kiralama_ucreti = ihaObject.saatlik_fiyati * kiralama_saatleri

        # kiralama kaydını oluşturun ve kaydedin
        
        kiralama_kaydi =kiralama(iha_id=ihaObject, user_id=userObject, kiralama_baslangic=startdate, kiralama_bitis=enddate, kiralama_ucret=kiralama_ucreti)
        kiralama_kaydi.save()
        data='{"status":true ,  "kiralama_ucreti":%d,"saatlik_fiyati":%d ,"iha_adi":"%s","resim":"%s" }' % (kiralama_ucreti,ihaObject.saatlik_fiyati,ihaObject.iha_adi,ihaObject.resim)
        return HttpResponse({data}, content_type="application/json")