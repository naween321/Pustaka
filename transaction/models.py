from django.db import models

from book.models import Book
from shared_app.models import Base
from django.contrib.auth.models import User


class Transaction(Base):
    STATUS = (
        ('REQUESTED', 'requested'),
        ('CANCELED', 'canceled'),
        ('REJECTED', 'rejected'),
        ('DECLINED', 'declined'),
        ('ON_DELIVERY', 'on_delivery'),
        ('OFFERED', 'offered'),
        ('EXCHANGED', 'exchanged')
    )

    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING, related_name='transactions')
    requested_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='transaction_requested_by',
                                     null=True)
    requested_to = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='transaction_requested_to',
                                     null=True)
    status = models.CharField(max_length=20, choices=STATUS, default='REQUESTED')
    exchanged_with = models.ForeignKey(Book, on_delete=models.DO_NOTHING, related_name='transaction_exchanged_books')


class TransactionLog(Base):
    STATUS = (
        ('REQUESTED', 'requested'),
        ('CANCELED', 'canceled'),
        ('REJECTED', 'rejected'),
        ('DECLINED', 'declined'),
        ('ON_DELIVERY', 'on_delivery'),
        ('OFFERED', 'offered'),
        ('EXCHANGED', 'exchanged')
    )

    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS, default='REQUESTED')
    exchange_with = models.ForeignKey(Book, on_delete=models.DO_NOTHING)
