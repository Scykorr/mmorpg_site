from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, CommentForm
from .models import Post, Comment, Person
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin


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

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        comments = Comment.objects.filter(post_id=self.kwargs['pk'])
        context['comments'] = comments
        return context


class PostCreate(LoginRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_update.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.method == 'POST':
             
             post.person_id = self.request.user.pk
        post.save()
        return super().form_valid(form)

    # def get_success_url(self):
    #     return reverse('lawyer_detail', kwargs={'lawyer_slug': self.object.lawyer_slug})

class PostUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('post.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_update.html'


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('post.delete_post',)
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


class CommentCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('comment.add_comment',)
    raise_exception = True
    form_class = CommentForm
    model = Comment
    template_name = 'comment_update.html'

    def form_valid(self, form):
        comment = form.save(commit=False)
        if self.request.method == 'POST':
             comment.person_id = self.request.user.pk
             comment.post_id = self.kwargs['pk']
        comment.save()
        return super().form_valid(form)
    
