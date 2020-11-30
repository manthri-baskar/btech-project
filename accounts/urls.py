from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUpView, name='signup'),
    path('signup/signed_up/', views.signed_up, name='signed_up')
]