from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.messages import constants
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect 
from django.urls import reverse
from django.contrib.auth import login

# Create your views here.

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
        # return HttpResponse('welcome back!')
    elif request.method == 'POST':
        email = request.POST.get('email')
        pwd = request.POST.get('password')
        if len(email.strip()) == 0 or len(pwd.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Try Again')
            return redirect(reverse('login'))
            
        user = auth.authenticate(email=email, password=pwd)
        # return HttpResponse(f'{email}, {pwd}')
        if not user:
            messages.add_message(request, constants.ERROR, 'Try Again')
            return redirect(reverse('login'))
        auth.login(request, user)
        return redirect('/users/main/')

def logout(request):
    logout(request),
    return redirect('/auth/login')
        
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
        # return HttpResponse('welcome back!')
    elif request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        pwd = request.POST.get('password')
        confirm_pwd = request.POST.get('confirm-password')
        
        if any(value.strip() == '' for value in [email, name, last_name, pwd, confirm_pwd]) or pwd != confirm_pwd or user.exists():
            messages.add_message(request, constants.ERROR, 'Invalid: try again. Make sure to correctly fill all empty spaces.')
            return redirect(reverse('register'))
        
        user = User.objects.create_user(email=email, password=pwd, first_name=name, last_name=last_name)
        messages.add_message(request, constants.SUCCESS, 'Invalid: try again. Make sure to correctly fill all empty spaces.')
        # return HttpResponse(f'{email}, {name}, {last_name}, {pwd}, {confirm_pwd}')
        return redirect(reverse('login'))

def fill_form(request):
    if request.method == 'GET':
        return render(request, 'main.html')
    elif request.method == 'POST':
        
        return redirect(reverse('login'))
