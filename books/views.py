from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import BooksForm, PublisherForm, AuthorForm

# Create your views here.


def lib(request):
    book = Books.objects.all()
    context = {'books': book}
    return render(request, 'books/home.html', context)


def pub(request):
    publisher = Publisher.objects.all()
    context = {'publishers': publisher}
    return render(request, 'books/list_publisher.html', context)


def aut(request):
    author = Authors.objects.all()
    context = {'authors': author}
    return render(request, 'books/list_author.html', context)


def book(request, pk):
    book = Books.objects.get(id=pk)
    context = {'books': book}
    return render(request, 'books/book.html', context)


def addBook(request):
    form = BooksForm()
    if request.method == 'POST':
        form = BooksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lib')

    context = {'form': form}
    return render(request, 'books/book_form.html', context)


def deleteBook(request, pk):
    book = Books.objects.get(id=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('lib')
    return render(request, 'books/delete.html', {
        'obj': book
    })


def editBook(request, pk):
    book = Books.objects.get(id=pk)
    form = BooksForm(instance=book)

    if request.method == 'POST':
        form = BooksForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('lib')
    context = {'form': form}
    return render(request, 'books/book_form.html', context)


def publishers(request):
    form = PublisherForm()
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lib')
    context = {'form': form}
    return render(request, 'books/publisher.html', context)


def author(request):
    form = AuthorForm()
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lib')
    context = {'form': form}
    return render(request, 'books/author.html', context)