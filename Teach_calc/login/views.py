from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    context ={
        "title" : "Вход",
    }
    return render(request,'login/login.html', context)

def register(request):
    return render (request, 'login/register.html')