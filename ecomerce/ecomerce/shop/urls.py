from django.urls import path

from ecomerce.shop.views import shop, single_product, cart, checkout

urlpatterns = [
    path('shop/', shop, name='shop'),
    path('product/', single_product, name='product'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),

]