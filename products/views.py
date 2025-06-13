from django.shortcuts import redirect, render
from .models import Product, Stock

def create_product(request):
    if request.method == 'POST':
        product = request.POST['product']
        description = request.POST['description']
        quantity = request.POST['quantity']
        price = request.POST['price']
        product = Product.objects.create(name=product, description=description)
        Stock.objects.create(product_id=product,quantity=quantity, price=price)
    return render(request, 'products/create_product.html')

def list_products(request):
    all_products = Product.objects.all()
    return render(request, "products/list_products.html", {'all_products':all_products})

def update_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        product.name = request.POST['product']
        product.description = request.POST['description']
        product.save()
        return redirect('list_products')
    return render(request, 'products/update_product.html', {'product': product})


def delete_product(request, product_id):
    product = Product.objects.get(id= product_id)
    product.delete()
    return redirect('list_products')

# Create your views here.
