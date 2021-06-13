from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime
from passsecure.models import secure,usertable
from cryptography.fernet import Fernet

# Create your views here.
def profile_detail(request, username=None):
    obj = get_object_or_404(User, username=username)
    user = obj.profile
    context = {
        "object": obj,
        "user": user,
    }
    return user

def generate_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
def load_key():
    """
    Loads the key named `secret.key` from the current directory.
    """
    return open("secret.key", "rb").read()

def index(request):
    if request.method=="POST":
        platform=request.POST.get("platform")
        accname=request.POST.get("accname") 
        accpassword=request.POST.get("accpassword")
       
       
        s = secure(platform=platform,accname=accname,accpassword=accpassword,date=datetime.today())
        s.save()
    return render(request,'index.html')


def register(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('register')

    else:
        f = UserCreationForm()

    return render(request, 'register.html', {'form': f})
    
def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        #s = usertable(username=username,password=password)
        #s.save()
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
def delt(request):
    labelid = request.GET.get("deleteid",False)
    a = secure.objects.get(id=labelid).delete()
    
    #secure.objects.all()
    return redirect("/pass")
def decrypt(request):
    #labelid = request.GET.get("decryptid",False)
    load_key()
    
    accpassword=request.GET.get("decryptid",False)
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(accpassword)
    s = secure(accpassword=decrypted_message)
    s.save()

#def store(request):
def passuser(request):
    #profile_detail(request)
    data = secure.objects.all()
    #data = secure.objects.filter(owner=user)
    return render(request,"pass.html", {"secure": data})

    return render(request,"pass.html")

  

        
       