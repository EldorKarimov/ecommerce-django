from carts.models import Cart, CartItem
from .views import _cart_id

def counter(request):
    
    cart_item_count = 0
    try:
        cart = Cart.objects.filter(cart_id = _cart_id(request))
        cart_items = CartItem.objects.filter(cart = cart[:1])
        for cart_item in cart_items:
            cart_item_count += cart_item.quantity
    except Cart.DoesNotExist:
        cart_item_count = 0
    return {'cart_item_count':cart_item_count}