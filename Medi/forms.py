from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class PostForm (forms.ModelForm):
    class Meta:
         model = Appointment

         exclude = ['middle_name']