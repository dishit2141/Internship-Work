
from django.contrib import admin
from django.urls import path,include
from home import views                     

urlpatterns = [
 
    path('',views.index,name='home'),
    #path('/login',views.login,name='loginuser'),
    path('logout',views.logoutuser,name='logout'),
    path('login',views.loginuser,name='login'),
    path('contact',views.contact,name='contact'),
    

]