from django.shortcuts import render, redirect

from book.models import Book
from transaction.models import Transaction


def book_request(request, **kwargs):
    owner_id = Book.objects.get(id=kwargs['book_id']).user_id
    Transaction.objects.create(book_id=kwargs['book_id'], requested_by_id=kwargs['user_id'], requested_to_id=owner_id)
    pass
    return redirect('home')


