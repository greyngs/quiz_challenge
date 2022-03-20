from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

def home(request):
    context = {'title' : "Home"}

    return render(request, 'home.html', context)

def register(request):
    if request.method == 'POST':
        form  = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'User {username} created')
            return redirect('home_process')
    else:
        form = UserRegisterForm()

    context = {'form' : form}
    return render(request, 'register.html', context)
