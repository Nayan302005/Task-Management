from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)

    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        deadline = request.POST['deadline']

        Task.objects.create(
            user=request.user,
            title=title,
            description=description,
            deadline=deadline
        )

        return redirect('dashboard')

    return render(request, 'dashboard.html', {'tasks': tasks})


@login_required
def complete_task(request, id):
    task = Task.objects.get(id=id)
    task.completed = True
    task.save()
    return redirect('dashboard')


@login_required
def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('dashboard')