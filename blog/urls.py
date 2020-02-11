# tunr/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('author/', views.author_list, name='author_list'),
    path('author/<int:pk>', views.author_detail, name='author_detail'),
    path('blog/<int:pk>', views.blog_detail, name='blog_detail'),
    path('', views.blog_list, name='blog_list'),
    path('author/new', views.author_form, name='author_form'),
    path('blog/new', views.blog_form, name='blog_form'),
    path('blog/delete/<int:pk>', views.blog_delete, name='blog_delete'),
    path('blog/edit/<int:pk>', views.blog_edit, name='blog_edit'),
    path('author/edit/<int:pk>', views.author_edit, name='author_edit')
]