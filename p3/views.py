from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Welcome to Index page")

def first(request):
    return render(request,"sample.html")

def second(request):
    return render(request,"directory/second.html")