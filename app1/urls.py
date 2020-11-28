from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('daily_business', views.daily_business),
    path('inventory_left', views.inventory_left),
    path('add_item', views.add_item)
]