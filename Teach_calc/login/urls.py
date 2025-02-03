from django.urls import path
from login import views

app_name = 'login'

urlpatterns = [
    path('', views.register, name = 'register'),
    path('login/', views.login, name = "login"),
    path('register/',views.register, name = "register")
]