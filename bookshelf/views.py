from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from bookshelf.models import Books
from bookshelf.forms import BookForm

# Create your views here.

class BookListView(ListView):
    model = Books


class CreateBookView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    form_class = BookForm

    model = Books
