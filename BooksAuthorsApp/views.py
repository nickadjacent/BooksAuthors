from django.shortcuts import render, redirect
from .models import *


def bookPage(request):
    context = {
        'books': Book.objects.all(),
    }
    print(Book.objects.all())
    print('opening to the book page')
    return render(request, 'bookPage.html', context)


def bookName(request):
    context = {
        'authors': Author.objects.all()
    }
    print(Author.objects.all())
    print('book name')
    return render(request, 'bookName.html', context)


def authorPage(request):
    context = {
        'authors': Author.objects.all()
    }
    print('adding an author')
    return render(request, 'authorPage.html', context)


def authorName(request):
    context = {
        'books': Book.objects.all()
    }
    print('book.objects.al()')
    print('author name')
    return render(request, 'authorName.html', context)


# ****************Everything Below is A redirect****************


def addBook(request):
    Book.objects.create(
        title=request.POST['title'],
        desc=request.POST['description'],
    )

    print('adding a book to the page')
    return redirect('/')


def addAuthor(request):
    Author.objects.create(
        first_name=request.POST['first name'],
        last_name=request.POST['last name'],
        notes=request.POST['notes'],
    )

    print('adding an Author to the page')
    return redirect('/authorPage')
