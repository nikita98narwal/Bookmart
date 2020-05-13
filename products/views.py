from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def details(request,id=1):
	product = Product.objects.get(id=id)
	return render(request, "details.html", {"product": product})