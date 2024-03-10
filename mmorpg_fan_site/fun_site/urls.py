from django.urls import path
# Импортируем созданное нами представление
from .views import PostsList, PostDetail, PostCreate, PostDelete, PostUpdate, CommentCreate, OwnCommentsList, CommentDelete, OwnPostsList, CommentUpdate


urlpatterns = [
    path('', PostsList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('create/',  PostCreate.as_view(), name='post_create'),
    path('<int:pk>/update/',  PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/',  PostDelete.as_view(), name='post_delete'),
    path('<int:pk>/comment/',  CommentCreate.as_view(), name='comment_update'),
    path('postsfilter/',  OwnPostsList.as_view(), name='posts_filter'),
    path('postsfilter/comments/<int:pk>/update/',  CommentUpdate.as_view(), name='comment_update'),
    path('postsfilter/<int:pk>/delete/',  PostDelete.as_view(), name='post_delete'),
    path('postsfilter/comments/',  OwnCommentsList.as_view(), name='comments_filter'),
    path('postsfilter/comments/<int:pk>/delete/',  CommentDelete.as_view(), name='post_delete'),
]
