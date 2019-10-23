from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import login as auth_login, logout as auth_logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm, CustomUserCreationForm


def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    form = CustomUserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        auth_login(request, user)
        return redirect('accounts:login')
    context = {'form': form}
    return render(request, 'accounts/form.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    form = AuthenticationForm(request, request.POST or None)
    if form.is_valid():
        auth_login(request, form.get_user())
        next_page = request.GET.get('next')
        return redirect(next_page or 'articles:index')
    context = {'form': form}
    return render(request, 'accounts/form.html', context)


def logout(request):
    auth_logout(request)
    return redirect('accounts:login')


@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
    return redirect('articles:index')
    # return redirect('aricles:index')


@login_required
def update(request):
    form = CustomUserChangeForm(request.POST or None, instance=request.user)
    # if request.method == 'POST':
    #     form = CustomUserChangeForm(request.POST, instance=request.user)
    if form.is_valid():
        form.save()
        return redirect('articles:index')
    # else:  # == 'GET'
    #     form = CustomUserChangeForm(instance=request.user)
    context = {'form': form}
    return render(request, 'accounts/form.html', context)


@login_required
def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('accounts:update')
    else:
        form = PasswordChangeForm(request.user)  # 다르다
    context = {'form': form}
    return render(request, 'accounts/form.html', context)
