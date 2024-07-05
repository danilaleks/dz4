from django.shortcuts import render, redirect
from .forms import ProductForm, Product

def home(request):
    products = Product.objects.all()
    new_products = Product.objects.filter(new=True)
    return render(request, 'home.html', {'products': products, 'new_products': new_products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})
