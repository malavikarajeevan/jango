from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
   
    path('contact/',views.contact,name='contact'),
    path('destinations/',views.destinations,name='destinations'),
    path('elements/',views.elements,name='elements'),
    path('index/',views.index,name='index'),
    path('news/',views.news,name='news')
    
    
    
]