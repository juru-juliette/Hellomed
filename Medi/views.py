# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from .models import Appointment
from .forms import PostForm
# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):
    # return HttpResponse('Welcome to Hellomed')
    return render(request, 'index.html')




@login_required(login_url='/accounts/login/')
def post(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            
            post.save()
        return redirect('home')

    else:
        form = PostForm()
    return render(request, 'post.html', {"form": form})