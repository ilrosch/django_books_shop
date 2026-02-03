from django.contrib import admin
from books.models import *


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'last_name', 'first_name', 'middle_name', 'created_at']


@admin.register(Genre)
class GenresAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    
    
@admin.register(Language)
class LanguagesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']


@admin.register(Book)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'author', 'language', 'genre', 'updated_at', 'created_at']
    
    
@admin.register(Order)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'updated_at', 'created_at']


@admin.register(OrderItem)
class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'item']