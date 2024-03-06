from django.urls import path
# Импортируем созданное нами представление
from .views import PostsList, PostDetail, create_post


urlpatterns = [
    path('', PostsList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    path('create/',  create_post, name='post_create'),
]
