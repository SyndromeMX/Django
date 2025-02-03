from django.urls import path
from login import views

app_name = 'login'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('login/', views.login, name = "login"),
]