from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Books


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'author', 'description', 'year', 'is_available']
