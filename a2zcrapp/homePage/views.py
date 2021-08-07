from django.shortcuts import render
from .models import allProducts
def home(request):
    if request.method=="GET":
        products=allProducts.objects.all().order_by('-product_rating')[:5]
        return render(request,"homePage/home.html",{'products':products})
def product(request):
    if request.method=="GET":
        products=allProducts.objects.all().order_by('-product_rating')[:5]
        return render(request,"homePage/home.html",{'products':products})
def search(request):
    if request.method=="POST":
        searched=request.POST["searched"]
        products=allProducts.objects.filter(product_name__contains=searched)
        return render(request,"homePage/home.html",{'products':products})
        

