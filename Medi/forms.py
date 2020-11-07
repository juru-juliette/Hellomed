# from django.contrib.auth import get_user_model
from django import forms
from .models import *
# check for unique email and username
class ProfileForm(forms.ModelForm):
    class Meta:
         model= Profile
