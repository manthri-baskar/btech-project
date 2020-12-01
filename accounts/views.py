from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.

def register(request):
    return render(request, 'register.html')

def regist(request):
    first_name      = request.POST["first_name"]
    last_name       = request.POST["last_name"]
    username        = request.POST["username"]
    email           = request.POST["email"]
    password1       = request.POST["password1"]
    password2       = request.POST["password2"]
 
    if password1==password2:
        
        if User.objects.filter(username=username).exists():
            return render(request,'register.html',{'message':'Account not created. This username is already in use. Choose another one.'})
        elif User.objects.filter(email=email).exists():
            return render(request,'register.html',{'message':'Account not created. This email is already in use. Choose another one.'})
        else:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
            user.save()

    else:
        return render(request,'register.html',{'message':'Account not created. Password is not confirmed.....'})

    return render(request,'register.html',{'message':'account created'})
