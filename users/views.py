from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from . forms import SignUpForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# Create your views here.
def register(request):
    form = SignUpForm()
    context = {
        'form':form
    }
    
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request,"users/register.html",{'form':form})
    return render(request,'users/register.html',context)

def loginuser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request,'Username or Password is incorrect')
    return render(request,"users/login.html")

def logoutuser(request):
    logout(request)
    return redirect('login')


def profile(request):
    return render(request,"users/profile.html")