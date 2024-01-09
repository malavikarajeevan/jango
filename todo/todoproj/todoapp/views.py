from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

# Create your views here.
def Home(req):
    tasks=Task.objects.all()
    if req.method=="POST":
        task=req.POST.get('task','')
        priority=req.POST.get('priority','')
        # print(task,priority)
        todo=Task(task=task,priority=priority)
        todo.save()
    return render(req,"index.html",{"tasks":tasks})

def update(req,id):
    print(id)
    task=Task.objects.get(id=id)
    return render(req,'update.html',{"task":task})
# def contact(req):
#     return render(req,"contact.html")
