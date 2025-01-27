from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
        "titile" : "Главная",
        "content" : "Главная страница"
    }
    return render(request,"main/index.html", context)

def about(request):
    return HttpResponse("About")

def register(request):
    return HttpResponse("reg")

def login(request):
    return HttpResponse("log")