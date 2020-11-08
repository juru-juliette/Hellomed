# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six
class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='photos/',null=True)
    fullname = models.CharField(max_length=255,null=True)
    username = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    phone_number = models.CharField(max_length = 10,blank =True)
    email=models.EmailField()

    def __str__(self):
        return self.username.username

    def save_profile(self):
        self.save()    
        
    def update_profile(self):
        self.update()

    def delete_profile(self):
        self.delete() 

class Yourmodel(models.Model):
    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)

   
class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active)
        )
account_activation_token = TokenGenerator()

class Appointment(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    condition = models.CharField(max_length=300)
    preferred_date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.first_name