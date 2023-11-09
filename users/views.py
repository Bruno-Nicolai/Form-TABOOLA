from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages, auth
from django.contrib.messages import constants
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect 
from django.urls import reverse

# Create your views here.
        
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        pwd = request.POST.get('password')
        confirm_pwd = request.POST.get('confirm_password')
      
        if pwd != confirm_pwd:
            messages.add_message(request, constants.ERROR, 'Passwords do not match.')
            return redirect(reverse('register'))
        new_user = User(username=username, password=pwd)
        user = User.objects.create_user(new_user)
        user.first_name = name
        user.last_name = last_name
        user.save()
        
        if not User.objects.filter(username=new_user.username).exists():
            messages.add_message(request, constants.SUCCESS, 'Your new account has just been added to our system.')
            return redirect('auth/main')
        else:
            messages.add_message(request, constants.ERROR, 'An error ocurred when trying to register the user. Please try again')
            return redirect(reverse('register'))

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('password')
            
        user = auth.authenticate(username=username, password=pwd)
        if not user:
            messages.add_message(request, constants.ERROR, 'Invalid Login Credentials')
            return redirect(reverse('login'))
        auth.login(request, user)
        return redirect('/auth/main/')

def logout(request):
    logout(request),
    return redirect('/auth/login')
        
        
def fill_form(request):
    if request.method == 'GET':
        return render(request, 'main.html')
    elif request.method == 'POST':
        return redirect(reverse('login'))
