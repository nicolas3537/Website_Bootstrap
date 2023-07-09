from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import TaskForm


# Create your views here.
def home(request):
    return render(request, 'home.html', {"nickname": 'nico'})

@login_required
def todolist(request):
    form = TaskForm()
    
    if request.method == "POST":
        form = TaskForm(request.POST)
        print("test")
        if form.is_valid():
            task = form.save(commit=False)
            task.author =request.user
            task.save()
            return redirect("todolist")
    
    
    tasks = Task.objects.filter(author=request.user)
    return render(request, "todolist.html", {"tasks": tasks, "task_form":form})

def update(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance= task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid :
            form.save()
            return redirect("todolist")
    return render(request, "update.html", {"edit_task_form": form})

def delete(request,pk):
    task = Task.objects.get(id=pk)
    if request.method == "POST":
        task.delete()
        return redirect("todolist")
    return render(request, "delete.html", {"task":task})