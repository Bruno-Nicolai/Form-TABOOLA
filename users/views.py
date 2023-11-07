from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect 

# Create your views here.

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
        # return HttpResponse('welcome back!')

def logout(request):
    logout(request),
    return redirect('/auth/login')
        
def register(request):
    return render(request, 'register.html')
