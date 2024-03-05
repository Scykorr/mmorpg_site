from django.shortcuts import render

from django.views.generic import ListView
from .models import Post


class PostsList(ListView):
    model = Post
    ordering = 'create_date'
    template_name = 'posts.html'
    context_object_name = 'posts'
