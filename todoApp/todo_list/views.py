from django.shortcuts import render, redirect, get_object_or_404
from .models import todo
from .forms import TodoForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = TodoForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redireciona após adicionar para evitar duplicação
    todos = todo.objects.all()
    form = TodoForm()
    return render(request, 'home.html', {'todos': todos, 'form': form})

def about(request):
    context = {'name': 'Gabriel Victor', 'age': 24}
    return render(request, 'about.html', context)

def delete_todo(request, todo_id):
    todo_item = get_object_or_404(todo, id=todo_id)
    todo_item.delete()
    return redirect('home')


def edit_todo(request, todo_id):
    todo_item = get_object_or_404(todo, id=todo_id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo_item)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TodoForm(instance=todo_item)
    return render(request, 'edit_todo.html', {'form': form, 'todo_id': todo_id})

