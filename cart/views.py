from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from cart.Cart import Cart
from myapp.models import Product
from cart.models import Cart as CartModel


def cart_add(request, product_id):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Unauthorized'}, status=401)

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        cart = Cart(request)
        cart.add(product)

        if request.user.is_authenticated:
            cart_item, created = CartModel.objects.get_or_create(
                user=request.user,
                product=product
            )
            if not created:
                cart_item.quantity = cart.cart.get(str(product.id), {}).get('quantity', 0)
            else:
                cart_item.quantity += 1
            cart_item.save()

        total_cart_count = cart.get_total_count()

        return JsonResponse({'cart_count': total_cart_count, 'message': 'Product added tp cart!'})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def cart_view(request):
    pass

def cart_count():
    pass

def cart_delete(request):
    pass

def cart_clear(request):
    pass
