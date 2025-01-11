from django.contrib.auth.views import LogoutView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, reverse_lazy

from . import views
from .views import ProfileUser, delete_user

app_name = 'users'
urlpatterns = [
    path('signup/', views.RegisterUser.as_view(), name='signup'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileUser.as_view(), name='profile'),
    path('change-password/', views.UserPasswordChange.as_view(), name='change_password'),
    #path('password-change/', views.UserPasswordChange.as_view(), name='password_change'),
    path('password-change/complete/', PasswordChangeDoneView.as_view(template_name="users/password_change_complete.html"), name='password_change_complete'),
    path('password-reset/done/', PasswordResetDoneView.as_view(), name='users/password_reset_done'),
    path('password-reset/', PasswordResetView.as_view(template_name="users/password_reset_form.html",
                                                      email_template_name="users/password_reset_email.html",
                                                      success_url=reverse_lazy("users:users/password_reset_done")), name='password_reset'),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html",
                                                                              success_url=reverse_lazy("users:password_reset_complete")), name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"), name='password_reset_complete'),
    path('delete-user/', delete_user, name='delete_user'),

]

