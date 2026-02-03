from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

dataPath = settings.BASE_DIR / 'books' / 'data'

class Author(models.Model):
    first_name = models.CharField(max_length=255, verbose_name="Имя")
    middle_name = models.CharField(max_length=255, blank=True, verbose_name="Отчество")
    last_name = models.CharField(max_length=255, verbose_name="Фамилия")
    updated_at = models.DateField(auto_now=True, verbose_name="Последнее обновление")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    
    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"
    
    
class Language(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    
    def __str__(self):
        return self.name
    
    
class Genre(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    
    def __str__(self):
        return self.name
    
    
class Book(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    year = models.PositiveIntegerField(verbose_name="Год")
    content = models.FileField(upload_to='books/data/contents', verbose_name="Текст книги", blank=True)
    front_cover = models.FileField(upload_to='books/data/images', verbose_name="Обложка книги", blank=True)
    language = models.ForeignKey(Language, on_delete=models.PROTECT, related_name="books", verbose_name="Язык")
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name="books", verbose_name="Жанр")
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name="books", verbose_name="Автор")
    updated_at = models.DateField(auto_now=True, verbose_name="Последнее обновление")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    
    def __str__(self):
        return f'{self.name} - {self.author}'
    
    
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders", verbose_name="Пользователь")
    updated_at = models.DateField(auto_now=True, verbose_name="Последнее обновление")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    
    def __str__(self):
        return f'{self.user} - {self.created_at}'
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order", verbose_name="Заказ")
    item = models.ForeignKey(Book, on_delete=models.PROTECT, related_name="order", verbose_name="Позиция")
    
    def __str__(self):
        return f'{self.order} - {self.item}'