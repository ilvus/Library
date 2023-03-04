from django.forms import ModelForm
from .models import Books, Publisher, Authors


class BooksForm(ModelForm):
    class Meta:
        model = Books
        fields = '__all__'


class PublisherForm(ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'


class AuthorForm(ModelForm):
    class Meta:
        model = Authors
        fields = '__all__'
