from django.contrib import admin
from books.models import *

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'last_name', 'first_name', 'middle_name', 'created_at']

@admin.register(Genre)
class GenresAdmin(admin.ModelAdmin):
    ...
    
@admin.register(Language)
class LanguagesAdmin(admin.ModelAdmin):
    ...

@admin.register(Book)
class BooksAdmin(admin.ModelAdmin):
    ...    
    
@admin.register(Order)
class OrdersAdmin(admin.ModelAdmin):
    ...
