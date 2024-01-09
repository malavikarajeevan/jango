from .import views
from django.urls import path

urlpatterns = [
     path('',views.Home,name='home'),
     # path('contact/',views.contact,name='contact')
     path('update/<int:id>',views.update,name='update'),
]
