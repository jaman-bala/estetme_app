from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


from .models import Panel
from .forms import CreateForm


@login_required
def index(request):
    todos = Panel.objects.all()
    return render(request, 'panel/index.html', {'todo_list': todos})


@login_required
def add(request):
    if request.method == 'POST':
        form = CreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateForm()
    return render(request, 'panel/create.html', {"form": form})


@login_required
def update(request, todo_id):
    todo = Panel.objects.get(id=todo_id)
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect('index')


@login_required
def edit(request, todo_id):
    todo = get_object_or_404(Panel, id=todo_id)
    if request.method == 'POST':
        form = CreateForm(request.POST, request.FILES, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateForm(instance=todo)
    return render(request, 'panel/create.html', {"form": form} )


@login_required
def delete(request, todo_id):
    todo = Panel.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')