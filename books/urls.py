from django.urls import path
from .views import *

urlpatterns = [
    path('', lib, name="lib"),
    path('add_book/', addBook, name='addbook'),
    path('delete_book/<str:pk>', deleteBook, name='delete-book'),
    path('edit_book/<str:pk>', editBook, name='edit-book'),
    path('book/<str:pk>', book, name='book'),
    path('publisher/', publishers, name='addpublisher'),
    path('author/', author, name='addauthor'),
    path('list_publisher/', pub, name='pub'),
    path('list_author/', aut, name='aut')

]