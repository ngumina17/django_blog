from django import forms
from .models import Author, Blog


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'location', 'photo_url',)


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'author', 'content', 'photo_url',)
        widgets = {'author': forms.HiddenInput()}


class SearchBar(forms.Form):
    fields = ('search')
