import datetime

from django.http import HttpResponse
from django.shortcuts import render
from books.models import Book, Publisher


def hello(request):
    return HttpResponse('Hello world')


def home_page(request):
    return HttpResponse('Home')


def current_time(request):
    now = datetime.datetime.now()
    return render(request,
                  'current_datetime.html',
                  {'current_date': now})


def book_list(request):
    books = Book.objects.all()
    return render(request,
                  'book_list.html',
                  {'books': books})

def publisher_list(request):
    publishers = Publisher.objects.all()
    return render(request,
                  'publishers.html',
                  {'publishers': publishers})
