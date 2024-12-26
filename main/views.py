from django.shortcuts import render, redirect
from .models import Books
from django.contrib.auth import login
from .forms import CustomUserCreationForm


def index(request):
    return render(request, 'main/index.html')


def books(request):
    books = Books.objects.all()
    return render(request, 'main/books.html', {'title': 'Все книги', 'books': books})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматический вход после регистрации
            return redirect('home')  # Перенаправление на главную страницу
    else:
        form = CustomUserCreationForm()
    return render(request, 'main/register.html', {'form': form})
