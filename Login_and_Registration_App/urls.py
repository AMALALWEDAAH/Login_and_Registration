from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	
    path('registre',views.register),
    path('login',views.login), 
    path('sucess',views.sucess),  
    path('logout',views.logout)
]