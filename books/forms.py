from django import forms
from books.models import *

class AuthorForm(forms.ModelForm):
    """Форма для создания/редактирования автора"""
    
    class Meta:
        model = Author
        fields = ['first_name', 'middle_name', 'last_name']
        widgets = {
            'first_name': forms.TextInput(),
            'middle_name': forms.TextInput(),
            'last_name': forms.TextInput(),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

class GenreForm(forms.ModelForm):
    """Форма для создания/редактирования жанра"""
    
    class Meta:
        model = Genre
        fields = ['name']
        widgets = {
            'name': forms.TextInput(),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

class LanguageForm(forms.ModelForm):
    """Форма для создания/редактирования языка"""
    
    class Meta:
        model = Language
        fields = ['name']
        widgets = {
            'name': forms.TextInput(),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

class BookForm(forms.ModelForm):
    """Форма для создания/редактирования книги"""
    
    class Meta:
        model = Book
        fields = ['name', 'description', 'author', 'price', 'language', 'year', 'genre', 'content', 'front_cover']
        widgets = {
            'name': forms.TextInput(),
            'description': forms.TextInput(),
            'year': forms.NumberInput(),
            'price': forms.NumberInput(),
            'author': forms.Select(),
            'language': forms.Select(),
            'genre': forms.Select(),
            'content': forms.FileInput(),
            'front_cover': forms.FileInput()
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].queryset = Author.objects.all()
        self.fields['language'].queryset = Language.objects.all()
        self.fields['genre'].queryset = Genre.objects.all()
        