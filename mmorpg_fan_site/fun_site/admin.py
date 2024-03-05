from django.contrib import admin

from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Post, Category, Comment, Person


class PostAdminForm(forms.ModelForm):
    text = forms.CharField(label='Текст', widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm


admin.site.register(Post, PostAdmin)
admin.site.register(Person)
admin.site.register(Comment)
admin.site.register(Category)
