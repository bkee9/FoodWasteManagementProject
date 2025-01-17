from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import resolve
from .forms import CreateUserForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.
def signin(request, template='Login.html'):
    next = request.GET.get('next')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request=request, username=username, password=password)
        if user:
            login(request, user)
            print("post data",request.POST)
            if request.GET.get('next'):
                url = request.GET.get("next", "")
                url = resolve(str(url))
                return HttpResponseRedirect('/add/')
            return redirect('home')
        error = 'Credentials do not match'
        return render(request, template, {'error': error})
    return render(request, template, {'next': next})

def register(request, template='Register.html'):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, template, {'form': form})
    form = CreateUserForm()
    return render(request, template)

def logout_user(request):
    logout(request)
    return redirect('home')

    