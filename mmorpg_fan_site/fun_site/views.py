from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from django.views.generic import ListView, DetailView, CreateView
from .forms import PostForm
from .models import Post
from django.contrib.auth.mixins import PermissionRequiredMixin


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


# @login_required
# def create_post(request):

#     form = PostForm()

#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/posts/')

#     return render(request, 'post_edit.html', {'form': form})

class PostCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('post.add_post',)
    raise_exception = True
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        return super().form_valid(form)

    # def get_success_url(self):
    #     return reverse('lawyer_detail', kwargs={'lawyer_slug': self.object.lawyer_slug})
