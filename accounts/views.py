from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout


def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        auth_login(request, user)
        return redirect('accounts:login')
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    form = AuthenticationForm(request, request.POST or None)
    if form.is_valid():
        auth_login(request, form.get_user())
        next_page = request.GET.get('next')
        return redirect(next_page or 'articles:index')
    context = {'form': form}
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('accounts:login')


@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
    return redirect('articles:index')
    # return redirect('aricles:index')


# def update(request):
    
