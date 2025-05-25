from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, label='Имя')
    last_name = forms.CharField(max_length=100, label='Фамилия')
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(), label='Пароль')
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(), label='Повторите пароль')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Имя'}), label='Имя')
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}), label='Пароль')
    remember_me = forms.BooleanField(required=False, label='Запомнить меня')