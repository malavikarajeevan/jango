from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

# Create your views here.
def Home(req):
    tasks=Task.objects.all()
    if req.method=="POST":
        task=req.POST["task"]
        priority=req.POST["priority"]
        # print(name,priority)
        todo=Task(task=task,priority=priority)
        todo.save
    return render(req,"index.html",{"tasks":tasks})
# def contact(req):
#     return render(req,"contact.html")
