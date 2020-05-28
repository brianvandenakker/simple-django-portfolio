from django.db import models
from django.urls import reverse

# Create your models here.
class Books(models.Model):
    book_title = models.CharField(max_length=128)
    book_author = models.CharField(max_length =128)
    book_link = models.URLField(max_length=512, null = True, blank = True)

    def __str__(self):
        return self.book_title

    def get_absolute_url(self):
        return reverse("bookshelf:books_list")
