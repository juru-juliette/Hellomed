# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .forms import *
# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    # return HttpResponse('Welcome to Hellomed')
    return render(request, 'index.html')

@login_required(login_url='/accounts/login/')
def profile(request, profile_id):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.username = current_user
            profile.save()
            return redirect('home')

    else:
        form = ProfileForm()
    username=User.objects.all()    
    myProfile = Profile.objects.filter(username = current_user) 
    
    return render(request, 'profile.html', {"form": form, "username": username,"myProfile": myProfile,}) 



