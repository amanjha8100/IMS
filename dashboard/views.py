from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . models import Product
from .forms import AddProduct

# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request,'dashboard/index.html')


@login_required(login_url='login')
def staff(request):
    return render(request,"dashboard/staff.html")

@login_required(login_url='login')
def product(request):
    form = AddProduct()
    return render(request,"dashboard/products.html",{'form':form})

@login_required(login_url='login')
def order(request):
    return render(request,"dashboard/order.html")