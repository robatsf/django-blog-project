from .models import profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class Registrationform(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email','password1','password2']
    

class userupdateform(forms.ModelForm):
    email=forms.EmailField()
     
    class Meta:
       model=User
       fields=['username','email']

class profileupdateform(forms.ModelForm):
    class Meta:
        model=profile
        fields=['image']