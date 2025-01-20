from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm
from django.contrib.auth.decorators import user_passes_test

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect

from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # بررسی نقش کاربر
            if user.role == 'user':
                return redirect('profile') 
            elif user.role == 'admin':
                return redirect('admin_dashboard')
            elif user.role == 'superuser':
                return redirect('/admin/')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid username or password.'})
    return render(request, 'accounts/login.html')


from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.role in ['admin', 'superuser'], login_url='login')
def admin_dashboard(request):
    return render(request, 'accounts/admin_dashboard.html')

def edit_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'accounts/edit_profile.html', {'form': form})

from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html', {'user': request.user})

# محدود کردن دسترسی فقط به ادمین
@user_passes_test(lambda u: u.role in ['admin', 'superuser'])
def admin_dashboard(request):
    return render(request, 'accounts/admin_dashboard.html')

