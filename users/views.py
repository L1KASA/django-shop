from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView

from djangoProject import settings
from .forms import NewUserForm, LoginUserForm, UserPasswordChangeForm, ProfileUserForm


class RegisterUser(CreateView):
    form_class = NewUserForm
    template_name = 'users/signup.html'
    extra_context = {'title': 'Регистрация'}
    success_url = reverse_lazy('users:login')

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Вход'}

    def get_success_url(self):
        return reverse('myapp:index')

class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'users/profile.html'
    extra_context = {
        'title': 'Профиль пользователя',
        'default_image': settings.DEFAULT_USER_IMAGE,
    }

    def get_success_url(self):
        return reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_tab'] = 'profile'
        context['edit_mode'] = self.request.GET.get('edit', 'false') == 'true'
        return context



class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy('users:password_change_complete')
    template_name = "users/password_change.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_tab'] = 'change_password'
        return context
