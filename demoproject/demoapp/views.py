from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(req):
    return render(req,'index.html')

def contact(req):
    return render(req,'contact.html')
def destinations(req):
    return render(req,'destinations.html')
def elements(req):
    return render(req,'elements.html')
def index(req):
    return render(req,'index.html')
def news(req):
    return render(req,'news.html')