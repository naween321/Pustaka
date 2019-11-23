from django.db import models

from django.contrib.auth.models import User
from shared_app.models import Base


class Author(Base):
    full_name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField(blank=True, null=True)


class Book(Base):
    STATUS =(
        ('AVAILABLE', 'Available'),
        ('RESERVED', 'reserved'),
        ('BEING_READ', 'being_read')
    )

    GENRE = (
        ('SCIENCE_FICTION', 'science_fiction'),
        ('TECHNOLOGY', 'technology'),
        ('ROMANCE', 'romance'),
        ('MYSTERY', 'mystery'),
        ('SELF_HELP', 'self_help'),
        ('FANTASY', 'fantasy'),
        ('HISTORY', 'history'),
        ('BIOGRAPHY', 'biography'),
        ('THRILLER', 'thriller'),
        ('TEXTBOOK', 'textbook'),
        ('OTHER', 'other')
    )

    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='book')
    status = models.CharField(max_length=20, choices=STATUS, default='AVAILABLE')
    authors = models.ManyToManyField(Author, through='BookAuthor')
    book_img = models.ImageField(upload_to='books/')
    genre = models.CharField(max_length=20,choices=GENRE)
    number_of_pages = models.IntegerField(null=True, blank=True)
    edition = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)


class BookAuthor(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
