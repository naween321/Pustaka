from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def user_register(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)

        if user_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data.get('username')
            messages.success(request, f'User is created for {username}')
            return redirect('/accounts/login/')
    else:
        user_form = UserCreationForm()
    return render(request, 'registration/new_user.html', {'form': user_form})


def home(request):
    return render(request, 'partial/base.html')
