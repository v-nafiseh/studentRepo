from ast import Delete
from curses import noecho
from urllib import response
from django.shortcuts import render
from rest_framework import viewsets

from manage.books.models import Book
from manage.books.serializers import BookSerializer
from rest_framework import response

class BookViewSet(viewsets.ViewSet):
    def list_all_books(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return response(serializer.data)

    def create_book(self, request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        publish('book_published', serializer.data)
        return response(serializer.data)

    def get_book(self, request, pk=None):
        book = Book.objects.get(id=pk)
        serializer = BookSerializer(book)
        return response(serializer.data)

    def update_book(self, request, pk=None):
        book = Book.objects.get(id=pk)
        serializer = BookSerializer(instance=book, data=request.data)
        serializer.save()
        return response(serializer.data)


