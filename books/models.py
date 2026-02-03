from django.db import models
from django.contrib.auth.models import User
# from django.conf import settings

class Author(models.Model):
    first_name = models.CharField(max_length=255, verbose_name="Имя")
    middle_name = models.CharField(max_length=255, blank=True, verbose_name="Отчество")
    last_name = models.CharField(max_length=255, verbose_name="Фамилия")
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"
    

class Language(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    
class Genre(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    year = models.PositiveIntegerField()
    # content = models.FilePathField(path="/", verbose_name="Текст книги")
    # front_cover = models.FilePathField(path="/", verbose_name="Обложка книги")
    language = models.ForeignKey(Language, on_delete=models.PROTECT, related_name="books")
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name="books")
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name="books")
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, related_name="orders")
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)