# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .email import send_welcome_email
from django.core.mail import send_mail
import datetime 
from .models import Appointment
from .forms import PostForm,NewsLetterForm
# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):
    # return HttpResponse('Welcome to Hellomed')
    return render(request, 'index.html')



def news_today(request):
    date = dt.date.today()
    news = Article.todays_news()
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('news_today')
    else:
        form = NewsLetterForm()
    return render(request, 'index.html', {"date": date,"news":news,"letterForm":form})

def article(request,article_id):
    try:
        article = Article.objects.get(id = article_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"newsletter/article.html", {"article":article})

def room(request, room_name):
    return render(request, 'chatroom.html', {
        'room_name': room_name
    })






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