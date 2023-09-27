from django import forms 
from django.forms import ModelForm, PasswordInput, CharField
from .models import Foydalanuvchi, Password

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = Password
        fields = ['foydalanuvchi_nomi', 'parol', 'veb_sayt']
        
