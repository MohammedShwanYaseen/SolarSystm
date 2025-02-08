from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import authenticate ,login ,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from .forms import SignUpForm,UpdateUserForm,ChangePasswordForm,UserInfoForm
from django import forms
from django.core.mail import send_mail
from solar.settings import EMAIL_HOST_USER
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import User, SolarPanel, Battery, SensorData, Report


def pro(request):
     if request.user.is_authenticated:
        current_user = Profile.objects.get(user__id=request.user.id)
        form = UserInfoForm(request.POST or None, instance=current_user)

        if form.is_valid():
             form.save()
             login(request,current_user)
             messages.success(request, ("Info is Updated "))
             return redirect('home')
        return render(request, 'pro.html', {"form":form})
     else:
          messages.success(request, ("You Must Be Logged In "))
          return redirect('home')
     

def request_user(request):
     if request.method =='POST':
        
        message_username =request.POST['username']
        message_itemname =request.POST['item-name']
        message_email =request.POST['email']
        message_address =request.POST['address']
        message_pictuer =request.POST['pictuer']
        message =request.POST['message']

        send_mail('message form ' + message_username ,
                  message + message_pictuer + message_address +message_itemname ,
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
            return redirect('pro')
        else:
            messages.success(request ,('There was problem registering please try again'))
            return redirect('register')


    else:    
        return render(request , 'register.html',{'form':form})
    


def get_user_dashboard(user_id):
    user_id = request.GET.get('id') 
    user = User.objects.get(id=user_id)
    user = get_object_or_404(User, id=user_id)
    if user.role == 'Owner':
        panels = user.panels.all()
        data = [{"panel_id": panel.panel_id, "location": panel.location, "capacity": panel.capacity} for panel in panels]
        return JsonResponse({"user": user.name, "role": user.role, "panels": data})
    elif user.role == 'Installer':
        all_panels = SolarPanel.objects.all()
        return JsonResponse({"user": user.name, "role": user.role, "panels_count": all_panels.count()})
    elif user.role == 'Admin':
        total_users = User.objects.count()
        return JsonResponse({"user": user.name, "role": user.role, "total_users": total_users})
    return JsonResponse({"error": "Invalid role"})


def generate_report(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if user.role == 'Owner':
        report_content = f"Energy report for {user.name}."
    elif user.role == 'Installer':
        report_content = f"System status overview for Installer {user.name}."
    elif user.role == 'Admin':
        report_content = f"Admin {user.name} has managed the system."
    else:
        return JsonResponse({"error": "Invalid role"})

    report = Report.objects.create(user=user, summary=report_content)
    return JsonResponse({"report_id": report.report_id, "summary": report.summary})


