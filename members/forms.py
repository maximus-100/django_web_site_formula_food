from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetForm, SetPasswordForm
from captcha.fields import CaptchaField
from web_site.models import Profile, Post


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditAccountForm(UserChangeForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))

    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = User
        fields = '__all__'


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio',
                  'profile_image',
                  'phone',
                  'mobile',
                  'address',
                  'website_url',
                  'github_url',
                  'instagram_url',
                  'facebook_url',
                  'telegram_url'
                  )

        widgets = {
            'bio': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'website_url': forms.TextInput(attrs={'class': 'form-control'}),
            'github_url': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
            'telegram_url': forms.TextInput(attrs={'class': 'form-control'})
        }


class SendResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        fields = '__all__'


class SetNewPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control'}
    ), label='Пароль')

    new_password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control'}
    ), label='ПОтвердите пароль')

    class Meta:
        fields = "__all__"


class EditForm(forms.ModelForm):
    class Meta:
        fields = ('title', 'content', 'photo')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'})
        }
