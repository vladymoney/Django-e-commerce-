from django.shortcuts import render

# Create your views here.

def shop(request):
    return render(request, 'shop.html')

def single_product(request):
    return render(request, 'product-single.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')
