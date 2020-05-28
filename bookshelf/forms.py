from django import forms
from bookshelf.models import Books


class BookForm(forms.ModelForm):

    class Meta:
        model = Books
        fields = ('book_title', 'book_author', 'book_link')

        widgets = {
            'book_title':forms.TextInput(attrs={'class':'textinputclass'}),
            'book_author':forms.TextInput(attrs={'class':'textinputclass'}),
            'book_link':forms.TextInput(attrs={'class':'textinputclass'}),
        }
