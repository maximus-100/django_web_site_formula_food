from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from .forms import (SignUpForm,
                    EditAccountForm,
                    ChangePasswordForm,
                    EditForm,
                    EditProfileForm,
                    SetNewPasswordForm,
                    SendResetForm)
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.views import (PasswordChangeView,
                                       PasswordResetView,
                                       PasswordResetForm,
                                       PasswordResetConfirmView)

from web_site.models import Profile, Post


# Create your views here.
class UserRegisterView(SuccessMessageMixin, CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    success_message = 'Регистрация прошла успешно. Войдите в акаунт.'


class UserEditAccountView(SuccessMessageMixin, UpdateView):
    form_class = EditAccountForm
    template_name = 'registration/change_account.html'
    success_url = reverse_lazy('change_account')
    success_message = 'Даннае изменены'

    def get_object(self, queryset=None):
        return self.request.user


class UserChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = 'registration/edit_password.html'
    success_url = reverse_lazy('change_account')
    success_message = 'Даннае пароли изменены'


class UserProfileView(ListView):
    model = Profile
    template_name = 'registration/profile.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        user = get_object_or_404(User, username=self.kwargs['username'])

        user_profile = Profile.objects.get(user=user)
        context = super().get_context_data()
        context['user_profile'] = user_profile

        return context


class UserEditProfileView(SuccessMessageMixin, UpdateView):
    form_class = EditProfileForm
    model = Profile
    template_name = 'registration/edit_profile.html'
    success_message = 'Данные профиля успешно изменены'

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'username': self.request.user.username})

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, user=self.request.user)


class UserResetPasswordView(SuccessMessageMixin, PasswordResetView):
    form_class = SendResetForm
    template_name = 'registration/reset_password.html'
    success_url = reverse_lazy('login')
    success_message = 'Проверти вашу почту'


class UserSetNewPasswordView(SuccessMessageMixin, PasswordResetConfirmView):
    form_class = SetNewPasswordForm
    template_name = 'registration/set_password.html'
    success_url = reverse_lazy('login')
    success_message = 'Ваш пороль успешна изменен'
