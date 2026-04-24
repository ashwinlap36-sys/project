from django.shortcuts import render, redirect
from .models import Task
from datetime import date


def home(request):
    tasks = Task.objects.all().order_by('task_date')
    today = date.today()

    return render(request, 'index.html', {
        'tasks': tasks,
        'today': today
    })


def add_task(request):
    if request.method == "POST":
        name = request.POST.get('name')
        task_date = request.POST.get('task_date')

        if name and task_date:
            Task.objects.create(
                name=name,
                task_date=task_date
            )

    return redirect('/')



def complete_task(request, id):
    task = Task.objects.get(id=id)
    task.completed = True
    task.save()

    return redirect('/')