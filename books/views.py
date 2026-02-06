from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from books.forms import *


def get_user_role(user):
    if not user.is_authenticated:
        return 'gust'
    if user.is_superuser:
        return 'admin'
    return 'user'


def books_page(req):
    user_role = get_user_role(req.user)
     
    books = Book.objects.select_related('author')
     
    if user_role in ['manager', 'admin']:
        search_value = req.GET.get('search', '')
        if search_value:
            books = books.filter(
                Q(name__icontains=search_value) |
                Q(description__icontains=search_value) |
                Q(author__first_name__icontains=search_value) |
                Q(author__last_name__icontains=search_value) |
                Q(genre__name__icontains=search_value) |
                Q(language__name__icontains=search_value)
            )
            
        sort_by = req.GET.get('sort', 'name-asc')
        match sort_by:
            case 'name-asc':
                books = books.order_by('name')
            case 'name-desc':
                books = books.order_by('-name')
            case 'price-asc':
                books = books.order_by('price')
            case 'price-desc':
                books = books.order_by('-price')
    
    paginator = Paginator(books, 4)
    page_num = req.GET.get('page')
    page_obj = paginator.get_page(page_num)
    
    return render(req, "index.html", context={
        "user_role": user_role,
        "page_obj": page_obj,
        "books": books,
        "sort": sort_by,
        "search_value": search_value,
    })


@login_required
def author_create(req):
    """Создание нового автора (только для администратора)"""

    if not req.user.is_superuser:
        messages.error(req, "У вас нет прав для выполнения этого действия.")
        return redirect("main:books")

    if req.method == "POST":
        form = AuthorForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, "Автор успешно добавлен.")
            return redirect("main:books")
    else:
        form = AuthorForm()
    
    return render(req, "form.html", {
        "form": form,
        "title": "Добавить автора"
    })


@login_required
def author_update(req, pk):
    """Редактирование автора (только для администратора)"""

    if not req.user.is_superuser:
        messages.error(req, "У вас нет прав для выполнения этого действия.")
        return redirect("main:books")

    author = get_object_or_404(Author, pk=pk)

    if req.method == "POST":
        form = AuthorForm(req.POST, instance=author)
        if form.is_valid():
            form.save()
            messages.success(req, "Автор успешно обновлен.")
            return redirect("main:books")
    else:
        form = AuthorForm(instance=author)
    
    return render(req, "form.html", {
        "form": form,
        "title": "Редактировать автора"
    })
    

@login_required
def book_create(req):
    """Создание новой книги (только для администратора)"""

    if not req.user.is_superuser:
        messages.error(req, "У вас нет прав для выполнения этого действия.")
        return redirect("main:books")

    if req.method == "POST":
        form = BookForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            messages.success(req, "Книга успешно добавлена.")
            return redirect("main:books")
    else:
        form = BookForm()
    
    return render(req, "form.html", {
        "form": form,
        "title": "Добавить книгу"
    })
    

@login_required
def book_update(req, pk):
    """Обновление книги (только для администратора)"""

    if not req.user.is_superuser:
        messages.error(req, "У вас нет прав для выполнения этого действия.")
        return redirect("main:books")
    
    book = get_object_or_404(Book, pk=pk)

    if req.method == "POST":
        form = BookForm(req.POST, req.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(req, "Книга успешно обновлена.")
            return redirect("main:books")
    else:
        form = BookForm(instance=book)
    
    return render(req, "form.html", {
        "form": form,
        "title": "Обновить книгу"
    })


@login_required
def genre_create(req):
    """Создание нового жанра (только для администратора)"""

    if not req.user.is_superuser:
        messages.error(req, "У вас нет прав для выполнения этого действия.")
        return redirect("main:books")

    if req.method == "POST":
        form = GenreForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, "Жанр успешно добавлен.")
            return redirect("main:books")
    else:
        form = GenreForm()
    
    return render(req, "form.html", {
        "form": form,
        "title": "Добавить жанр"
    })


@login_required
def genre_update(req, pk):
    """Обновление жанра (только для администратора)"""

    if not req.user.is_superuser:
        messages.error(req, "У вас нет прав для выполнения этого действия.")
        return redirect("main:books")
    
    genre = get_object_or_404(Genre, pk=pk)

    if req.method == "POST":
        form = GenreForm(req.POST, instance=genre)
        if form.is_valid():
            form.save()
            messages.success(req, "Жанр успешно обновлена.")
            return redirect("main:books")
    else:
        form = GenreForm(instance=genre)
    
    return render(req, "form.html", {
        "form": form,
        "title": "Обновить жанр"
    })


@login_required
def language_create(req):
    """Создание нового языка (только для администратора)"""

    if not req.user.is_superuser:
        messages.error(req, "У вас нет прав для выполнения этого действия.")
        return redirect("main:books")

    if req.method == "POST":
        form = LanguageForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, "Язык успешно добавлен.")
            return redirect("main:books")
    else:
        form = LanguageForm()
    
    return render(req, "form.html", {
        "form": form,
        "title": "Добавить язык"
    })
    

@login_required
def language_update(req, pk):
    """Обновление язык (только для администратора)"""

    if not req.user.is_superuser:
        messages.error(req, "У вас нет прав для выполнения этого действия.")
        return redirect("main:books")
    
    lang = get_object_or_404(Language, pk=pk)

    if req.method == "POST":
        form = LanguageForm(req.POST, instance=lang)
        if form.is_valid():
            form.save()
            messages.success(req, "Язык успешно обновлена.")
            return redirect("main:books")
    else:
        form = LanguageForm(instance=lang)
    
    return render(req, "form.html", {
        "form": form,
        "title": "Обновить язык"
    })