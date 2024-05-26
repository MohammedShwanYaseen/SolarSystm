from django.shortcuts import render, redirect
from .models import Post,Category
from django.contrib.auth import authenticate ,login ,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from .forms import SignUpForm,UpdateUserForm,ChangePasswordForm
from django import forms
from django.core.mail import send_mail


def request_user(request):
     if request.method =='POST':
        
        message_username =request.POST['username']
        message_itemname =request.POST['item-name']
        message_email =request.POST['email']
        message_address =request.POST['address']
        message =request.POST['message']

        send_mail('message form' + message_username,
                  message,
                  message_email,
                  ['mohammedshwan76@gmail.com'])
        return render(request,'request.html',{'message_username':message_username})

     else:
          return render(request,'request.html',{})
          

    
       
     


def search(request):
     if request.method == 'POST':
          searched =request.POST[ 'searched' ]
          searched = Post.objects.filter(item_name__icontains=searched)
          return render(request,'search.html',{"searched":searched})
     
     else: 
          return render(request,'search.html',{})

def password(request):
    if request.user.is_authenticated:
          current_user = request.user
          if request.method == 'POST':
               form = ChangePasswordForm(current_user,request.POST)
               if form.is_valid():
                    form.save()
                    login(request,current_user)
                    messages.success(request, ("Password change successfully"))
                    return redirect('login')
                    
               else:
                    for error in list(form.errors.values()):
                         messages.error(request, error) 
                         return redirect('password') 
               
          else:
              form = ChangePasswordForm(current_user)
              return render(request, 'password.html', {"form":form})
    else:
         messages.success(request, ("You Must Be Logged In"))
         
                  


def update_user(request):
     if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)

        if user_form.is_valid():
             user_form.save()
             login(request,current_user)
             messages.success(request, ("Info is Updated "))
             return redirect('home')
        return render(request, 'update_user.html', {"user_form":user_form})
     else:
          messages.success(request, ("You Must Be Logged In "))
          return redirect('home')
          	

def category_summary(request):
	categories = Category.objects.all()
	return render(request, 'category_summary.html', {"categories":categories})	

def category(request,foo):
	foo = foo.replace('-', ' ')
	try:
		category = Category.objects.get(category_name =foo)
		posts = Post.objects.filter(category=category)
		return render(request, 'category.html', {'posts':posts})
	except:
		messages.success(request, ("That Category Doesn't Exist..."))
		return redirect('home')


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


