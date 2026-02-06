from django.urls import path, include
from books.views import *

app_name = 'main'

urlpatterns = [
    path('', books_page, name='books'),
    path('authors/', include([
        path('create/', author_create, name='create_author'),
        path('update/<int:pk>/', author_update, name='update_author'),
    ])),
    path('books/', include([
        path('create/', book_create, name='create_book'),
        path('update/<int:pk>/', book_update, name='update_book'),
    ])),
    path('genre/', include([
        path('create/', genre_create, name='create_genre'),
        path('update/<int:pk>/', genre_update, name='update_genre'),
    ])),
        path('lang/', include([
        path('create/', language_create, name='create_lang'),
        path('update/<int:pk>/', language_update, name='update_lang'),
    ])),
]