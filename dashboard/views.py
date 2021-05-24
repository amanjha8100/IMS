from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . models import Product
from .forms import AddProduct
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request,'dashboard/index.html')


@login_required(login_url='login')
def staff(request):
    workers = User.objects.all()
    context = {
        'staff':workers,
    }
    return render(request,"dashboard/staff.html",context)


@login_required(login_url='login')
def staffdetail(request, pk):
    return render(request, 'dashboard/staffdetail.com')

@login_required(login_url='login')
def product(request):
    pro = Product.objects.all()
    form = AddProduct()
    if request.method == "POST":
        form = AddProduct(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product')
        else:
            return render(request,"dashboard/products.html",{'form':form,'product':pro})
    
    return render(request,"dashboard/products.html",{'form':form,'product':pro})

@login_required(login_url='login')
def order(request):
    return render(request,"dashboard/order.html")


@login_required(login_url='login')
def dele(request, pk):
    q = Product.objects.filter(pk=pk)
    q.delete()
    return redirect('product')


@login_required(login_url='login')
def edit(request, pk):
    item = Product.objects.get(pk=pk)
    form = AddProduct(instance=item)
    if request.method == "POST":
        form = AddProduct(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('product')
        else:
            return render(request,'dashboard/edit.html',{'form':form})
    return render(request,'dashboard/edit.html',{'form':form})