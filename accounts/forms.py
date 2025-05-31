from re import L
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile




class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, label='Имя', widget=forms.TextInput(
        attrs={"class": "form-control mb-1", 'placeholder': 'Введите Имя'}))
    last_name = forms.CharField(max_length=100, label='Фамилия', widget=forms.TextInput(
        attrs={"class": "form-control mb-1", 'placeholder': 'Введите Фамилию'}))
    username = forms.CharField(max_length=100, label='Логин', widget=forms.TextInput(
        attrs={"class": "form-control mb-1", 'placeholder': 'Введите Логин'}))
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"class": "form-control mb-1", 'placeholder': 'Введите Email'}))
    password1 = forms.CharField(max_length=50, label='Пароль', widget=forms.PasswordInput(
        attrs={"class": "form-control mb-1", 'placeholder': 'Введите Пароль'}))
    password2 = forms.CharField(max_length=50, label='Повторите пароль', widget=forms.PasswordInput(
        attrs={"class": "form-control mb-1", 'placeholder': 'Подтвердите Пароль'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']



class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True, label='Логин',
                               widget=forms.TextInput(attrs={"class": "form-control mb-1", 'placeholder': 'Ваш логин'}))
    password = forms.CharField(max_length=50,
                               required=True, label='Пароль',
                               widget=forms.PasswordInput(
                                   attrs={"class": "form-control mb-1", 'placeholder': 'Введите пароль'}))
    remember_me = forms.BooleanField(required=False, label='Запомнить меня')

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True, label='Логин',
                               widget=forms.TextInput(attrs={"class": "form-control mb-1", 'placeholder': 'Ваш логин'}))
    email = forms.EmailField(required=True, label='Email',
                             widget=forms.TextInput(attrs={"class": "form-control mb-1", 'placeholder': 'Ваш Email'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(label='Аватар', widget=forms.FileInput(attrs={"class": "form-control mb-1"}))
    bio = forms.CharField(label='О себе', widget=forms.Textarea(attrs={"class": "form-control"}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']