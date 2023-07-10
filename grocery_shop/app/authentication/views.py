# inventory/views.py
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('dashboard')
    else:
        form = AuthenticationForm(request)
    return render(request, '../templates/login.html', {'form': form})


@login_required
def dashboard_view(request):
    return render(request, '../templates/home.html')


def logout_view(request):
    logout(request)
    return redirect('login')
