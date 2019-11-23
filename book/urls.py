from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('add-new-book/', views.add_new_book, name='add-new-book'),
    path('book-list/', views.BookList.as_view(), name='book-list'),
    path('book-detail/<int:pk>', views.BookDetail.as_view(), name='book-detail')
]
