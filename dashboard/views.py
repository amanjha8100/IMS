from django.shortcuts import redirect, render
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