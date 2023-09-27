

from django.shortcuts import render, redirect
from .models import Password, User
from .forms import CustomUserCreationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # Redirect to the home page after signup
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def password_list(request):
    passwords = Password.objects.filter(user=request.user)
    print(passwords)
    return render(request, 'passwords/password_list.html', {'passwords': passwords})


def log_out(request):
    logout(request)
    return redirect('login')


def add_password(request):
    user = User.objects.all()
    form = CustomUserCreationForm(request.POST, request.FILES)
    if form.is_valid():
        password = form.save(commit=False)
        password.user = request.user
        form = password.save()
        return redirect('kk/')
    else:
        form = CustomUserCreationForm()

    return render(request, 'passwords/password_form.html', {'form': form, 'user':user})
    
    
def password_list(request):
    soz = request.GET.get('q', '')
    search=None
    if soz is not None:
        soz = soz.strip()
    
    if bool(soz.strip().replace(' ','')):
        search = Password.objects.filter(veb_sayt__startswith=soz,user=request.user).order_by('veb_sayt')
    elif not search:
        search = Password.objects.filter(user=request.user)
    return render(request, 'passwords/password_list.html', {'q':soz, 'natijalar':search})
