from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from passsecure import views                     

urlpatterns = [
 
    path('',views.index,name='passsecure'),
    
    path('logout',views.logoutuser,name='logout'),
    path('login',views.loginuser,name='login'),
    path('index',views.index,name='index'),
    path('pass',views.passuser,name='pass'),
    path('delt',views.delt,name='delt'),
    path('decrypt',views.decrypt,name='decrypt'),
    path('register', views.register, name='register'),
    


    
    

]