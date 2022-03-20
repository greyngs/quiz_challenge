from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from API.models import History

def home(request):
    context = {'title' : "Quiz"}
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

def history(request):
    records = list(reversed(History.objects.filter(user=request.user).values()))

    context = {'title' : "History", "records" : records}
    return render(request, 'history.html', context)

def ranking(request):
    records = list(History.objects.all().order_by('-score'))

    context = {'title' : "Ranking", "records" : records[:10]}
    return render(request, 'ranking.html', context)
