from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Task

# Create your views here.


def todo(request):
    obj = Task.objects.all()
    context = {'obj': obj}
    if request.POST:
        data = request.POST.get('todolist')
        task = Task(name=data)
        task.save()
        return redirect('todo')

    return render(request, 'todo.html', context)

def delet(request,pk):
    obj=Task.objects.get(id=pk)
    obj.delete()
    return redirect('todo')


    return render(request,'todo.html')
