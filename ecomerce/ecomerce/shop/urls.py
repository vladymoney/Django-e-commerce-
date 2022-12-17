from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from ecomerce.shop.views import shop, single_product, cart, checkout, add_photo

urlpatterns = [
    path('shop/', shop, name='shop'),
    path('product/', single_product, name='product'),
    path(
        'cart/', cart, name='cart'),
            path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
            path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
            path('cart/item_increment/<int:id>/',
                views.item_increment, name='item_increment'),
            path('cart/item_decrement/<int:id>/',
                views.item_decrement, name='item_decrement'),
            path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
            path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    path('checkout/', checkout, name='checkout'),
    path("add/", add_photo, name="add-photo"),


]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)