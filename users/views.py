from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from . forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
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

def profile_update(request):
    userform = UserUpdateForm()
    profileform = ProfileUpdateForm()
    if request.method == "POST":
        userform = UserUpdateForm(request.POST, instance=request.user)
        profileform = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            profileform.save()
            return redirect('profile')
        else:
            return render(request,'users/profile_update.html',{'userform':userform,'profileform':profileform})
    else:
        userform = UserUpdateForm(instance=request.user)
        profileform = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'userform':userform,
        'profileform':profileform,
    }
    return render(request,'users/profile_update.html',context)