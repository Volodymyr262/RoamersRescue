from django.urls import path, include
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('login-user/', views.loginUser, name='login-user'),
path('logout-user/', views.logoutUser, name='logout-user'),
path('register-user/', views.registerPage, name='register-user'),
path('verification/', include('verify_email.urls')),
path('activate/<uidb64>/<token>', views.activate, name='activate'),

path('post/<str:pk>/', views.postView, name='post'),

path('profile/<str:pk>/', views.profile, name='profile')
]