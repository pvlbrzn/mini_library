from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='home'),
    path('books', views.books, name='books'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='main/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('after-login/', views.after_login_redirect, name='after_login'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('return/<int:book_id>/', views.return_book, name='return_book'),
    path('return_manager/<int:book_id>/', views.return_book_manager, name='return_book_manager'),
    path('add_book/', views.add_book, name='add_book'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
]
