from django.shortcuts import render, redirect
from .models import Books
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'main/index.html')


@login_required
def books(request):
    books = Books.objects.all()
    context = {
        'title': 'Все книги',
        'books': books
    }
    return render(request, 'main/books.html', context=context)


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматический вход после регистрации
            return redirect('home')  # Перенаправление на главную страницу
    else:
        form = CustomUserCreationForm()
        context = {
            'form': form,
            'title': 'Регистрация'
        }
    return render(request, 'main/register.html', context=context)


@login_required
def after_login_redirect(request):
    if request.user.is_staff:
        return redirect('/admin/')
    return redirect('/')
