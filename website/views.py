from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *



def AboutPage(request):
    return render(request,'website/about.html')

def ContactPage(request):
    return render(request,'website/contact.html')

def HomePage(request):
    return render(request,'website/home.html')