from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from .forms import NewUserForm

class RegisterUser(CreateView):
    form_class = NewUserForm
    template_name = 'users/signup.html'
    extra_context = {'title': 'Регистрация'}
    success_url = reverse_lazy('users:login')

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Вход'}

    def get_success_url(self):
        return reverse('myapp:index')
