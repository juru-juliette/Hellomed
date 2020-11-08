# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):
    # return HttpResponse('Welcome to Hellomed')
    return render(request, 'index.html')
