from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
        "title" : "Главная страница",
        "content" : "Это мой первый веб сайт на фремворке Django. До этого я писал код на чистом html. Приложение представляет из себя базу для упрощения работы репетиторов и подсчета заработка и часов, а также расписание и часы работы"
        }

    return render(request,"main/index.html", context)
    
def about(request):
    context = {
        "title" : "О нас",
        "content" : "Меня зовут Владислав я хочу стать хорошим программистом."
        }
    return render(request, "main/about.html", context)

