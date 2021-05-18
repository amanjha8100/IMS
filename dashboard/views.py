from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'dashboard/index.html')



def staff(request):
    return render(request,"dashboard/staff.html")


def product(request):
    return render(request,"dashboard/products.html")


def order(request):
    return render(request,"dashboard/order.html")