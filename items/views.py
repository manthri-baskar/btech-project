from django.shortcuts import render,redirect
from .models import additem

# Create your views here.

def addditem(request):
    return render(request,'add_item.html')
    
def added_item(request):

    Item_name              = request.POST["Item_name"]
    Order_advertisment_cost= request.POST["Order_advertisment_cost"]
    Transportation_cost    = request.POST["Transportation_cost"]
    Anti_deteriorate_cost  = request.POST["Anti_deteriorate_cost"]
    Usable_time            = request.POST["Usable_time"]
    Lead_time              = request.POST["Lead_time"]

    additem_info = additem(Item_name=Item_name,Order_advertisment_cost=Order_advertisment_cost,Transportation_cost=Transportation_cost,Anti_deteriorate_cost=Anti_deteriorate_cost,Usable_time=Usable_time,Lead_time=Lead_time)

    additem_info.save()
    return redirect('/items/add_item')

def dailybusiness(request):
    return render(request,'dailybusiness.html')

def inventoryleft(request):
    return render(request,'inventoryleft.html')