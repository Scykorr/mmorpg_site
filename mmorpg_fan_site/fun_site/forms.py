from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'category',
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'text',

        ]


class CommentUpdForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'is_fix',

        ]