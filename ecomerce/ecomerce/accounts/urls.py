from django.urls import path

from ecomerce.accounts.views import Singin, Singup, logout_request

urlpatterns = [
    path('singin/', Singin.as_view(), name='login'),
    path('singup/', Singup.as_view(), name='register'),
    path("logout", logout_request, name="logout"),

]