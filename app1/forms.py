from django import forms
from django.core.exceptions import ValidationError
from django.db.models import fields

from .models import additem

class additemform(forms.ModelForm):
    class Meta:
        model = additem
        fields='__all__'
