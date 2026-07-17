from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from todolist.models import Tasklist
from todolist.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance =form.save(commit=False)
            instance.Owner = request.user
            instance.save()
            messages.success(request,("New Task Added!"))
        else:
            messages.warning(request,"Please enter the new task you want to add!")

        return redirect('todolist')
    
    
    else:
        all_tasks = Tasklist.objects.filter(Owner=request.user)
        paginator= Paginator(all_tasks,10)
        page = request.GET.get('pg')
        all_tasks =paginator.get_page(page)
        
        return render(request,'todolist.html',{'all_tasks':all_tasks})


@login_required    
def edit_task(request,task_id):
    if request.method =="POST":
        task =Tasklist.objects.get(pk=task_id)
        form =TaskForm(request.POST or None,instance=task)
        if form.is_valid():
            form.save()
        messages.success(request,('Task Edited!'))
        return redirect("todolist")
    else:
        task_obj =Tasklist.objects.get(pk=task_id)
        return render(request,'edit.html',{'task_obj':task_obj})

#only use to render html
def about(request):
    return render(request, "about.html")

#used if we want to pass some value to html
def contact(request):
    context = {
        'contact_text':"Welcome to the Contact"
    }
    return render(request,'contactus.html',context)

def index(request):
    context = {
        'index_text':"Welcome to the Taskmate"
    }
    return render(request,'index.html',context)

@login_required
def complete(request,task_id):
    # task = Tasklist.objects.get(pk=task_id)
    task = get_object_or_404(Tasklist, pk=task_id, Owner=request.user)
    # if task.Owner == request.user:
    task.done = True
    task.save()
    # else:
        # messages.error(request,"Access Restricted,You are not allowed")
    return redirect('todolist')

@login_required
def pending(request,task_id):
    # task = Tasklist.objects.get(pk=task_id)
    task = get_object_or_404(Tasklist, pk=task_id, Owner=request.user)
    # if task.Owner == request.user:
    task.done = False
    task.save()
    # else:
    #     messages.error(request,"Access Restricted,You are not allowed")
    return redirect('todolist')

@login_required
def delete_task(request,task_id):
    task = get_object_or_404(Tasklist, pk=task_id, Owner=request.user)
    # if task.Owner == request.user:
    task = Tasklist.objects.get(pk=task_id)
    task.delete()
    # else:
    #     messages.error(request,"Access Restricted,You are not allowed")
    return redirect('todolist')
 