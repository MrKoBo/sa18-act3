from django.shortcuts import render
from .models import Products
from django.shortcuts import get_object_or_404

# Create your views here.
def product_list(request):
    products = Products.objects.all()
    return render(request, 'products/index.html', {'products': products})



def product_show(request, id):
    product = get_object_or_404(Products, id=id)
    return render(request, 'products/show.html', {'product': product})
