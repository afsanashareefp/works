from django.contrib import messages, auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
# appname/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View
from social_core.pipeline import user


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:

            return redirect('/')
        else:
            error_message = "Invalid username or password"
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')


def Register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username is taken")
                return render(request, 'register.html')

            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();

        else:
            messages.info(request,"Password is not matching")
            return render(request,'register.html')
        return render(request,'details.html')
    return render(request, "register.html")


def logout(request):
    auth.login(request,user)
    return redirect('/')