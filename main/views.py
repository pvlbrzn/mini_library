from django.shortcuts import render, redirect, get_object_or_404
from .models import Books
from .forms import UserRegistrationForm, BookForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages


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


def book_detail(request, pk):
    book = get_object_or_404(Books, pk=pk)
    return render(request, 'main/book_detail.html', {'book': book})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт для {username} успешно создан! Теперь вы можете войти.')
            return redirect('login')  # Замените на имя вашего URL для входа
    else:
        form = UserRegistrationForm()
    return render(request, 'main/register.html', {'form': form})


@login_required
def after_login_redirect(request):
    if request.user.is_staff:
        return redirect('/admin/')
    return redirect('/')


@login_required
def user_dashboard(request):
    user_books = Books.objects.filter(borrowed_by=request.user)
    available_books = Books.objects.filter(is_available=True)
    return render(request, 'main/user_dashboard.html', {
        'user_books': user_books,
        'available_books': available_books,
    })


@login_required
@user_passes_test(lambda u: u.is_staff)
def return_book_manager(request, book_id):
    book = get_object_or_404(Books, id=book_id)
    if not book.is_available:
        book.return_book()
        messages.success(request, f'Книга "{book.title}" была успешно возвращена в библиотеку.')
    else:
        messages.warning(request, f'Книга "{book.title}" уже доступна.')
    return redirect('books')


@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Books, id=book_id)
    if book.is_available:
        book.is_available = False
        book.borrowed_by = request.user
        book.save()
    return redirect('user_dashboard')


@login_required
def return_book(request, book_id):
    book = get_object_or_404(Books, id=book_id, borrowed_by=request.user)
    book.is_available = True
    book.borrowed_by = None
    book.save()
    return redirect('user_dashboard')


@user_passes_test(lambda u: u.is_staff)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Книга успешно добавлена.')
            return redirect('books')
    else:
        form = BookForm()
    return render(request, 'main/add_book.html', {'form': form})
