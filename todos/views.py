from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem
from .forms import TodoItemForm

def todo_list(request):
    todos = TodoItem.objects.all()
    return render(request, 'todos/todo_list.html', {'todos': todos})

def todo_detail(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    return render(request, 'todos/todo_detail.html', {'todo': todo})

def todo_create(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoItemForm()
    return render(request, 'todos/todo_form.html', {'form': form})

def todo_update(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    if request.method == 'POST':
        form = TodoItemForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoItemForm(instance=todo)
    return render(request, 'todos/todo_form.html', {'form': form})

def todo_delete(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todos/todo_confirm_delete.html', {'todo': todo})
