from datetime import datetime
from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .forms import PostForm
from .models import Post


class PostsList(ListView):
    model = Post
    ordering = 'create_date'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now()
        context['attention'] = 'Внимание! Поднимаем онлайн!'
        return context
    """
    -create_date' - обратная сортировка
    queryset = Products.objects.filter(price__lt=300) цена меньше чем 300 вместо ordering
    """


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


def create_post(request):
    form = PostForm()
    return render(request, 'post_edit.html', {'form': form})
