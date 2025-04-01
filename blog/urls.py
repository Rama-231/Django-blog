from django.contrib import admin
from django.urls import path,include
from blog import views

urlpatterns = [
    path('',views.blogHome,name='blogHome'),
    path('postContent',views.postContent,name='postContent'),
    path('<str:slug>',views.blogPost,name='blogPost'),
]