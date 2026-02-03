from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from books.forms import *

def books_page(req):
    return render(req, "index.html")

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
    
    return render(req, "author_form.html", {
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
    
    return render(req, "author_form.html", {
        "form": form,
        "author": author,
        "title": "Редактировать автора"
    })