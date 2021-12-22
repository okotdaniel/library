
from django.urls import path
from . views import book_view

urlpatterns = [
    
    path('', book_view, name="book-view"),
    
]
