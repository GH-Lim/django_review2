from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout


def signup(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('accounts:login')
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)


def login(request):
    form = AuthenticationForm(request, request.POST or None)
    if form.is_valid():
        auth_login(request, form.get_user())
        return redirect('articles:index')
    context = {'form': form}
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('accounts:login')
