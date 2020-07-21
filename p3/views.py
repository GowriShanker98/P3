from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Welcome to Index page")

def first(request):
    return render(request,"sample.html")

def second(request):
    return render(request,"directory/second.html")

def third(request):
    return render(request,"directory/third.html",context={'data':"Gowri",'name':"Shanker"})

def fourth(request):
    Fruits=['apple','banana','mango','kiwi','orange']
    return render(request,"directory/fourth.html",{'Fruits':Fruits}) 

def fifth(request):
    return render(request,"directory/fifth.html",{'a':10,'b':20}) 