# appname/urls.py
from django.urls import path
from . import views

app_name = 'credentials'

urlpatterns = [
    path('login/', views.Login, name='login'),
    path('register/', views.Register, name='register'),
    path('logout', views.logout, name='logout'),

]
