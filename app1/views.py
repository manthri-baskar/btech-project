from django.shortcuts import render, redirect
from .models import additem
from .forms import additemform
# Create your views here.

def home(request):
    return render(request,'home.html',{'name':'shop'})

def daily_business(request):
    return render(request,'dailybusiness.html')

def inventory_left(request):
    return render(request,'inventoryleft.html')

def add_item(request):
        form=additemform()
        if request.method == 'POST':
            form=additemform(request.POST) 
            if form.is_valid():
                form.save()
                return redirect('home.html')
                    
        return render(request,'add_item.html',context={'name':form})
    

    
