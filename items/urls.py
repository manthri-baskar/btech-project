from django.urls import path
from . import views

urlpatterns = [
    path('add_item/', views.addditem, name='additem'),
    path('add_item/added_item/', views.added_item, name='added_item'),
    path('daily_business/', views.dailybusiness, name='dailybusiness'),
    path('inventory_left/', views.inventoryleft, name='inventoryleft')
]