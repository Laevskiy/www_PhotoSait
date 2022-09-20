from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render (request,'site_photo_001.html')

def about(request):
    return render (request,'site_photo_about_me.html')

def price(request):
    return render (request,'site_photo_price.html')