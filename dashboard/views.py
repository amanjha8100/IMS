from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request,'dashboard/index.html')


@login_required(login_url='login')
def staff(request):
    return render(request,"dashboard/staff.html")

@login_required(login_url='login')
def product(request):
    return render(request,"dashboard/products.html")

@login_required(login_url='login')
def order(request):
    return render(request,"dashboard/order.html")