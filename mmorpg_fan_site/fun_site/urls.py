from django.urls import path
# Импортируем созданное нами представление
from .views import PostsList, PostDetail, PostCreate


urlpatterns = [
    path('', PostsList.as_view()),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('create/',  PostCreate.as_view(), name='post_create'),
]
