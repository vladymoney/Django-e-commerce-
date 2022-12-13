from django.urls import path

from ecomerce.common.views import index, about, blog, contact

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),

]