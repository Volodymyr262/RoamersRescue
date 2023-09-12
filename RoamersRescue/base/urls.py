from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('login-user/', views.loginUser, name='login-user'),
path('logout-user/', views.logoutUser, name='logout-user'),
path('register-user/', views.registerPage, name='register-user'),
]