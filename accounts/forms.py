from django.forms import ModelForm
from .models import order

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class orderForm(ModelForm):
    class Meta:
        model = order
        fields =  '__all__'

class createUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1' , 'password2']