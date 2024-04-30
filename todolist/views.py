from django.shortcuts import render, redirect
from django.http import HttpResponse 
from todolist.models import TaskList
from todolist.form import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def todolist(request):
    if request.method=="POST":
        form=TaskForm(request.POST or None)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.manage=request.user
            instance.save()
        messages.success(request,('Added Successfully!'))
        return redirect('todolist')
    else:
        all_tasks=TaskList.objects.all()
        paginator=Paginator(all_tasks,3)
        page=request.GET.get('pg')
        all_tasks=paginator.get_page(page)
        
        
        return render(request,'todolist.html',{'all_tasks':all_tasks})

def delete_task(request,task_id):
    task=TaskList.objects.get(pk=task_id)
    task.delete()
    return redirect('todolist')

def edit_task(request,task_id):
    if request.method=="POST":
        task=TaskList.objects.get(pk=task_id)
        form =TaskForm(request.POST or None,instance=task)
        if form.is_valid():
            form.save()
        messages.success(request,('Added Successfully!'))
        return redirect('todolist')
    else:
        task_obj=TaskList.objects.get(pk=task_id)
        return render(request,'edit.html',{'task_obj':task_obj})
    
def complete_task(request,task_id):
    task=TaskList.objects.get(pk=task_id)
    task.done=True
    task.save()
    return redirect('todolist')

def pending_task(request,task_id):
    task=TaskList.objects.get(pk=task_id)
    task.done=False
    task.save()
    return redirect('todolist')

def index(request):
    context={
        'index_text':"Welcome all to my Home page!"
    }
    return render(request,'index.html',context)




def contact(request):
    context={
        'contact_text':"Welcome all to my contact page!"
    }
    return render(request,'contact.html',context)

def about(request):
    context={
        'about_text':"Welcome all to my about page!"
    }
    return render(request,'about.html',context)


