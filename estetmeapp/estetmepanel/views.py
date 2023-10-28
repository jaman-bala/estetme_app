from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required


from .models import Panel
from .forms import CreateForm


@login_required
def index(request):
    todos = Panel.objects.all()
    return render(request, 'panel/index.html', {'todo_list': todos})


@require_http_methods(['POST'])
@csrf_exempt
def add(request):
    if request.method == 'POST':
        form = CreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        error = 'Формат был неверной'
        form = CreateForm()
        data = {
            'form': form,
            'error': error
        }
    return render(request, 'panel/index.html', {"data": data})


def update(request, todo_id):
    todo = Panel.objects.get(id=todo_id)
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect('index')


def delete(request, todo_id):
    todo = Panel.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')