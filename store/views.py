from django.shortcuts import get_object_or_404, render

from .models import Product
from category.models import Category

def store(request, slug=None):
    categories = None
    product = None
    if slug is not None:
        category = get_object_or_404(Category, slug=slug)
        product = Product.objects.filter(category=category, is_available=True)
        product_count = product.count()
    else:
        product = Product.objects.filter(is_available=True)
        product_count = product.count()
        
    context = {
        'products':product,
        'product_count':product_count,
    }
    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    context = {
        'product':product
    }
    return render(request, 'store/store_detail.html', context)