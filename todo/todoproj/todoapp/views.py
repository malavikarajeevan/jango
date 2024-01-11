from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
from .forms import forms

# Create your views here.
def Home(req):
    tasks=Task.objects.all()
    print(req.method)
    if req.method=="POST":

        task=req.POST.get('task','')
        priority=req.POST.get('priority','')
        date=req.POST.get('date','')
        img=req.FILES['image']
        # print(task,priority)
        todo=Task(task=task,priority=priority,date=date,image=img)
        todo.save()
    return render(req,"index.html",{"tasks":tasks})

def update(req,id):
    # print(id)
    # task=Task.objects.get(id=id)
    # if req.method=="POST":
    #     task=req.POST.get('task','')
    #     priority=req.POST.get('priority','')
    #     Task.objects.filter(id=id).update(task=task,priority=priority)
    #     return redirect("home")
    #=========================================
    #django forms
    f=TodoForm(req,POST or None,instance=tasks)
    if f.is_valid():
        f.save()
        return redirect("home")
    
    # return render(req,'update.html',{"task":task})
    return render(req, 'formupdate.html',{"task":tasks,'f':f})

def delete(req,id):
    task=Task.objects.get(id=id)
    if req.method=="POST":
        Task.objects.filter(id=id).delete()
        return redirect("home")
    return render(req,'delete.html',{"task":task})
    
 
# def contact(req):
#     return render(req,"contact.html")
