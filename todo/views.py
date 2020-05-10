from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .models import Todo
from .forms import TodoForm
# Create your views here.

def todo_list_view(request):
    todos = Todo.objects.all()
    return render(request, 'todo/todo.html', {'todos':todos})

def add_todo_view(request):
    new_todo = Todo()
    new_todo.text = request.POST['content']
    if request.POST['deadline']:
        new_todo.deadline = request.POST['deadline']
    new_todo.save()
    return redirect('/todo/') 

def delete_todo(request, pk):
    wbd_todo = Todo.objects.get(pk=pk)
    wbd_todo.delete()
    return redirect('/todo/')
