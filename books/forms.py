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