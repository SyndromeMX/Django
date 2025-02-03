from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def login(request):
    content ={
        "title" : "О нас",
        "content" : "Меня зовут Владислав я хочу стать хорошим программистом."
    }
    return render(request,'login/index.html', content)