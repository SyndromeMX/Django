from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def login(request):
    context ={
        "title" : "Вход",
    }
    return render(request,'login/login.html', context)


def register(request):
    if request.method == "POST":
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")

        if password != password_confirm:
            messages.error(request, "Пароли не совпадают.")
            return render(request, "register.html")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Пользователь с таким никнеймом уже существует.")
            return render(request, "register.html")

        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        messages.success(request, "Вы успешно зарегистрированы! Войдите в систему.")
        return redirect("login:login")

    return render(request, "login/register.html")