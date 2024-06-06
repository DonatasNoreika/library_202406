from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, BookInstance, Author
import datetime


# Create your views here.
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status='g').count()
    num_authors = Author.objects.all().count()
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'now': datetime.datetime.today(),
    }
    return render(request, template_name="index.html", context=context)


def authors(request):
    authors = Author.objects.all()
    context = {
        "authors": authors,
    }
    return render(request, template_name="authors.html", context=context)


def author(request, author_id):
    author = Author.objects.get(pk=author_id)
    context = {
        'author': author,
    }
    return render(request, template_name="author.html", context=context)
