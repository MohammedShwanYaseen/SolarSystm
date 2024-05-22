from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

def home(request):
    return render(request,'home.html'{})

