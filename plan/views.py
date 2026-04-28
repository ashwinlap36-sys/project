from django.shortcuts import render, redirect
from .models import Task
from datetime import date
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    tasks = Task.objects.filter(user=request.user).order_by('task_date')
    today = date.today()

    return render(request, 'index.html', {
        'tasks': tasks,
        'today': today
    })


@login_required
def add_task(request):
    if request.method == "POST":
        name = request.POST.get('name')
        task_date = request.POST.get('task_date')

        if name and task_date:
            Task.objects.create(
                name=name,
                task_date=task_date,
                user=request.user   # ✅ link task to user
            )

    return redirect('/')



def complete_task(request, id):
    task = Task.objects.get(id=id)
    task.completed = True
    task.save()

    return redirect('/')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already exists'})

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('home')

    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')