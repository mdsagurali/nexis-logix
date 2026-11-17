
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

from .forms import ProductForm
from .models import Product


# Home View
@login_required
@never_cache
def home(request):
    return render(request, 'invApp/home.html')


# Create Product
@login_required
@never_cache
def product_create_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(
        request,
        'invApp/product_form.html',
        {'form': form}
    )


# Read / List Products
@login_required
@never_cache
def product_list_view(request):
    products = Product.objects.all()

    return render(
        request,
        'invApp/product_list.html',
        {'products': products}
    )


# Update Product
@login_required
@never_cache
def product_update_view(request, product_id):
    product = get_object_or_404(
        Product,
        product_id=product_id
    )

    if request.method == 'POST':
        form = ProductForm(
            request.POST,
            instance=product
        )

        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)

    return render(
        request,
        'invApp/product_form.html',
        {'form': form}
    )


# Delete Product
@login_required
@never_cache
def product_delete_view(request, product_id):
    product = get_object_or_404(
        Product,
        product_id=product_id
    )

    if request.method == 'POST':
        product.delete()
        return redirect('product_list')

    return render(
        request,
        'invApp/product_confirm_delete.html',
        {'product': product}
    )
