from django.shortcuts import render,redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login 
from django.contrib import messages
from datetime import datetime
from .models import Contact
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')
    
def loginuser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
             login(request,user)
             return redirect("/")
        else:
             messages.info(request , 'invalid credentials')
             return render(request, 'login.html')
    return render(request, 'login.html')
def logoutuser(request):
    logout(request)
    return redirect("/login")

def contact(request):
   
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        msg=request.POST.get("msg")
        contact = Contact(name=name,email=email,phone=phone,msg=msg,date=datetime.today())
        contact.save()
        messages.success(request,"your message is been sent")
    return render(request,"contact.html")
def display(request):
    data = Contact.objects.all()
    context={'data':data}
    return render(request,"../contact.html",context)
