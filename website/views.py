from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def home(request):
    if request.method == 'POST':
        cpf = request.POST['cpf']
        password = request.POST['password']
        user = authenticate(request, username=cpf, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Cpf ou senha incorretos.", extra_tags='alert-warning')
            return redirect('home')
    else:
        return render(request, 'home.html', {})

def login_user(request):
    pass

def logout_user(request):
    pass