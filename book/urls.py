from django.urls import path
from . import views


urlpatterns = [
    path('add-new-book/', views.add_new_book, name='add-new-book'),
    path('', views.BookList.as_view(), name='home'),
    path('book-detail/<int:pk>', views.BookDetail.as_view(), name='book-detail')
]
