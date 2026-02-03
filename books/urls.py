from django.urls import path, include
from books.views import *

app_name = 'main'

urlpatterns = [
    path('', books_page, name='books'),
    path('authors/', include([
        path('create/', author_create, name='create_author'),
        path('update/<int:pk>/', author_update, name='update_author'),
    ])),
]