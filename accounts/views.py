from django.shortcuts import render, redirect
from .models import register

# Sign Up View
def SignUpView(request):
    return render(request,"signup.html")

def signed_up(request):

    First_name      = request.POST.get("First_name",False)
    Last_name       = request.POST.get("Last_name",False)
    Username        = request.POST.get("Username",False)
    Email_ID        = request.POST.get("Email_ID",False)
    Password        = request.POST.get("Password",False)
    Confirm_password= request.POST.get("Confirm_password",False)

    register_info = register(First_name=First_name, Last_name=Last_name, Username=Username, Email_ID=Email_ID, Password=Password, Confirm_password=Confirm_password)

    register_info.save()
    return render(request,"signup.html")
