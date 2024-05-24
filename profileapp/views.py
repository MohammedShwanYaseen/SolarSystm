from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth import authenticate ,login ,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from .forms import SignUpForm
from django import forms


def post(request,pk):
    post = Post.objects.get(id=pk)
    return render(request,'post.html',{'post':post})

def home(request):
    posts = Post.objects.all()
    return render(request,'home.html',{'posts':posts})

def about(request):
    return render(request, 'about.html', {})

def login_user(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request ,username=username ,password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('YOU HAVE BEEN LOGGIN '))
            return redirect('home')
        else:
            messages.success(request ,('YOUR USERNAME OR PASSWORD WRONG'))
            return redirect('login') 
    else:
           
         return render(request, 'login.html', {})
    
    

def logout_user(request):
    logout(request)
    messages.success(request, ('Thank you for visiting!'))
    return redirect('home')

def register_user(request):
    form = SignUpForm()
    if request.method =='POST':
        form =SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data ['username']
            password = form.cleaned_data ['password1']
            User = authenticate(username =username, password =password)
            login(request,User)
            messages.success(request ,('Thank you for register to user website'))
            return redirect('home')
        else:
            messages.success(request ,('There was problem registering please try again'))
            return redirect('register')


    else:    
        return render(request , 'register.html',{'form':form})


