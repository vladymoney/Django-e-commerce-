from profile import Profile

from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth import views as auth_views, get_user_model, login
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import logout
from django.shortcuts import redirect

from ecomerce.accounts.forms import UserCreateForm

UserModel = get_user_model()
# Create your views here.


class Singin(auth_views.LoginView):
    template_name = 'login.html'



class Singup(views.CreateView):
    template_name = 'register.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('index')




def my_view(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username


def logout_request(request):
	logout(request)
	return redirect("index")

