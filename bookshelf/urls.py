from django.urls import path, include
from . import views

app_name = 'bookshelf'

urlpatterns = [
#BLOG URLS
    path('', views.BookListView.as_view(), name='books_list'),
    path('add/', views.CreateBookView.as_view(), name='add_book')
]
