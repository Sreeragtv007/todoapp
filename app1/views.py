from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Task
from .form import TaskForm

# Create your views here.


def todo(request):
    obj = Task.objects.all()
    context = {'obj': obj}
    if request.GET:
        data = request.GET.get('todolist')
        task = Task(name=data)
        task.save()
        return redirect('todo')

    return render(request, 'todo.html', context)

def delet(request,pk):
    obj=Task.objects.get(id=pk)
    obj.delete()
    return redirect('todo')


    return render(request,'todo.html')



def update(request,pk):
    obj=Task.objects.get(id=pk)
    form=TaskForm(instance=obj)
    context={'form':form}
    if request.POST:
        form=TaskForm(request.POST,instance=obj)
        if form.is_valid:
            form.save()
            return redirect('todo')
    
    
    return render(request,'update.html',context)