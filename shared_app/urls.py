from django.urls import path

from shared_app import views

urlpatterns = [
    path('accounts/register/', views.user_register, name='user-register'),
    path('', views.home, name='home')
]
