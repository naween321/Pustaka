from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('add-new-book/', views.add_new_book, name='add-new-book')
]
