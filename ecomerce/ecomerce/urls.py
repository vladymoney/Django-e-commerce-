
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ecomerce.common.urls')),
    path('shop/', include('ecomerce.shop.urls')),
    path('accounts/', include('ecomerce.accounts.urls')),
]
