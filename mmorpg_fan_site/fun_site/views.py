from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, CommentForm, CommentUpdForm
from .models import Post, Comment, Person
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters import FilterSet


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
        comments = Comment.objects.filter(post_id=self.kwargs['pk'], is_fix=True)
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

class PostUpdate(LoginRequiredMixin, UpdateView):
    # permission_required = ('post.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_update.html'


class PostDelete(LoginRequiredMixin, DeleteView):
    # permission_required = ('post.delete_post',)
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts_filter')


class CommentCreate(LoginRequiredMixin, CreateView):
    # permission_required = ('comment.add_comment',)
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
    

class OwnCommentsList(LoginRequiredMixin, ListView):
    model = Comment
    ordering = ['create_date']
    template_name = 'comments_filter.html'
    context_object_name = 'commentsown'


    def get_queryset(self):
       queryset = Comment.objects.filter(post__person_id=self.request.user.id)
       self.filterset = PostFilter(self.request.GET, queryset, request=self.request.user.id)
       if self.request.GET:
            return self.filterset.qs
       return Comment.objects.none()

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now()
        # comments = Comment.objects.filter(post__person=self.request.user.id)
        # context['commentsown'] = comments
        
        
        context['filterset'] = self.filterset
        return context
    

class CommentDelete(LoginRequiredMixin, DeleteView):
    # permission_required = ('comment.delete_comment',)
    model = Comment
    template_name = 'comment_delete.html'
    success_url = reverse_lazy('comments_filter')
    


class OwnPostsList(LoginRequiredMixin, ListView):
    model = Post
    ordering = 'create_date'
    template_name = 'posts_filter.html'
    context_object_name = 'postsown'
    paginate_by = 3

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now()
        context['postsown'] = Post.objects.filter(person=self.request.user.pk)
        return context
    

class CommentUpdate(LoginRequiredMixin, UpdateView):
    # permission_required = ('post.change_post',)
    form_class = CommentUpdForm
    model = Comment
    template_name = 'comment_update.html'


class PostFilter(FilterSet):
    class Meta:
        model = Comment
        fields = [
            'post'
        ]

    def __init__(self, *args, **kwargs):
        super(PostFilter, self).__init__(*args, **kwargs)
        self.filters['post'].queryset = Post.objects.filter(person_id=kwargs['request'])