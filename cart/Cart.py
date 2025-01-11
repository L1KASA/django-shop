from cart.models import Cart as CartModel


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.get('cart', {})

        if request.user.is_authenticated:
            self.restore_from_db(request.user)


        if not self.cart:
            self.cart = {}

        self.save()

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'price': str(product.price),
                'quantity': 0,
                'product_name': product.name,
            }

        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def save(self):
        self.session['cart'] = self.cart
        self.session.modified = True

    def get_total_count(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_cart(self):
        return self.cart

    def restore_from_db(self, user):
        cart_items = CartModel.objects.filter(user=user)
        for cart_item in cart_items:
            product_id = str(cart_item.product.id)
            if product_id not in self.cart:
                self.cart[product_id] = {
                    'price': str(cart_item.product.price),
                    'quantity': cart_item.quantity,
                    'product_name': cart_item.product.name
                }