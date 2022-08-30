from django.urls import path
from .views import *
from django.contrib.auth import views

urlpatterns = [
    path('register', UserRegisterView.as_view(), name='register'),
    path('change_account/', UserEditAccountView.as_view(), name='change_account'),
    path('password/', UserChangePasswordView.as_view(), name='password'),

    path('reset-password/', UserResetPasswordView.as_view(), name='reset-password'),
    path('reset/<uidb64>/token/', UserSetNewPasswordView.as_view()),
    path('profile/<str:username>', UserProfileView.as_view(), name='profile'),
    path('edit_profile/<str:username>', UserEditProfileView.as_view(), name='edit_profile')
]
