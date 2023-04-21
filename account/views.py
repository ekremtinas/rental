from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login as auth_login
from django.contrib.auth.models import User
# Create your views here.
def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]

        user = authenticate(request, username=username,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect("home")
        else:
           return render(request,"login.html",{
            "error":"username or password not found"
           })
         
    return render(request,"login.html")

def register(request):
    if request.method=="POST":
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        repassword=request.POST["repassword"]
       

        if repassword==password:
            if(User.objects.filter(username=username).exists()):
                 return render(request,"register.html",{
                "error":"user exits"
             })
            else:
                 if(User.objects.filter(email=email).exists()):
                    return render(request,"register.html",{
                    "error":"email exits"
                    })
                 else:
                    user = User.objects.create(username=username,email=email,password=password)
                    user.save()
                    return redirect("login")

        else:
             return render(request,"register.html",{
                "error":"password and repassword not equal"
             })



    return render(request,"register.html")
