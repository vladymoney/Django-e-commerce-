from django.shortcuts import render
from django.contrib.auth import views as auth_views, get_user_model, login
from django.urls import reverse_lazy
from django.views import generic as views

from ecomerce.accounts.forms import UserCreateForm

UserModel = get_user_model()
# Create your views here.


class Singin(auth_views.LoginView):
    template_name = 'login.html'


class Singup(views.CreateView):
    template_name = 'register.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('index')
