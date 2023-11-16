from django.urls import path

from .views import *


urlpatterns = [
    path('about', AboutPage, name='about'),
    path('contact', ContactPage, name='contact'),
    path('home', HomePage, name='home'),
    
]
