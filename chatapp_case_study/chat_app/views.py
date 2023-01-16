import openai
from pymongo import MongoClient
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
import os
from django.conf import settings
from django.http import HttpResponse
from .models import *
from .forms import *
from django.shortcuts import render, redirect
import requests
from django.contrib.auth.decorators import login_required


openai.api_key = "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"


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            mobile_number = form.cleaned_data.get("mobile_number")
            password = form.cleaned_data.get("password")
            user = User.objects.filter(email=email)
            if user:
                return HttpResponse(f"{email} is already registered")
            user = User(name=name, email=email, mobile_number=mobile_number)
            user.set_password(password)
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, email = username, password = password)
        print(user)
        if user is not None:
            request.session['user_id'] = user.id
            form = login(request, user)
            return redirect('home')
        else:
            return redirect('register')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    request.session.flush() 
    return redirect('home')


def chat(request):
    if not request.user.is_anonymous:
        if request.method == 'POST':
            msg = request.POST['msg']
            user = request.user
            Chat.objects.create(user=user, author=user.name, message= msg)
            response = generate_response(msg)
            if response:
                message = response
            else:
                message = "Something wrong.."

            Chat.objects.create(user=user, author="GPT ", message= message)
            all_chats = Chat.objects.filter(user=user).order_by('timestamp')
            return render(request, 'chat.html', {'all_chats': all_chats})

        return render(request, 'chat.html')

    else:
        return redirect('login')
    

def generate_response(prompt): 
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = completions.choices[0].text
    return message.strip()
