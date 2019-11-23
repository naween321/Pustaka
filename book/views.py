from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from book.models import Book, Author, BookAuthor


@login_required
def home(request):
    books = Book.objects.all()
    return render(request, 'book/home.html', {'books': books})


def add_new_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        genre = request.POST.get('genre')
        number_of_pages = request.POST.get('number_of_pages')
        edition = request.POST.get('edition')
        description = request.POST.get('description')
        author = request.POST.get('author')
        user = request.user

        author = Author.objects.create(full_name=author)
        book = Book.objects.create(title=title, genre=genre, number_of_pages=number_of_pages,
                            edition=edition, description=description, user=user)
        BookAuthor.objects.create(author=author, book=book)
        return redirect('home')
    return render(request, 'book/add_new_book.html')


@method_decorator(login_required, name='dispatch')
class BookList(ListView):
    model = Book
    queryset = Book.objects.all()
    paginate_by = 10
    # template_name = 'book/list.html'
    template_name = 'book/detail.html'
    context_object_name = 'books'


@method_decorator(login_required, name='dispatch')
class BookDetail(DetailView):
    model = Book
    template_name = ''