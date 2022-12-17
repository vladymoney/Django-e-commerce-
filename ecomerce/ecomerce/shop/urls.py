from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from ecomerce.shop.views import shop, single_product, cart, checkout, add_photo

urlpatterns = [
    path('shop/', shop, name='shop'),
    path('cart/', cart, name='cart'),
    path('product/', single_product, name='product'),
    path('checkout/', checkout, name='checkout'),
    path("add/", add_photo, name="add-photo"),


]
