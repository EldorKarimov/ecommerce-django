from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Product
from category.models import Category
from carts.models import CartItem
from carts.views import _cart_id

def store(request, slug=None):
    categories = None
    product = None
    if slug is not None:
        search_item = request.GET.get('search_product')
        if search_item:
            product = Product.objects.filter(product_name__icontains=search_item, is_available=True)
        else:
            category = get_object_or_404(Category, slug=slug)
            product = Product.objects.filter(category=category, is_available=True)
        paginator = Paginator(product, 9)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        product_count = paginator.count
    else:
        search_item = request.GET.get('search_product')
        
        if search_item:
            product = Product.objects.filter(is_available=True, product_name__icontains=search_item)
        else:
            product = Product.objects.filter(is_available=True)
        
        paginator = Paginator(product, 9)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        product_count = page_obj.object_list.count
        
    context = {
        'products':page_obj,
        'product_count':product_count,
    }
    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id = _cart_id(request), product = product).exists()
        
    except Exception as e:
        raise e
    context = {
        'product':product,
        'in_cart':in_cart
    }
    return render(request, 'store/store_detail.html', context) 