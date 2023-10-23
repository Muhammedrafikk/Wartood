from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('blog/',views.blog,name='blog'),
    path('blogdetails/',views.blogdetails,name='blogdetails'),
    path('contact/',views.contact,name='contact'),
    path('project/',views.project,name='project'),
    path('service/',views.service,name='service'),
    path('servicedetails/<int:id>/',views.servicedetails,name='servicedetails')       
]