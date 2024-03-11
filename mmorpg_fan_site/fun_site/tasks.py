from celery import shared_task
from .models import Comment
from django.core.mail import send_mail


@shared_task
def comment_send_email(comment_id):
    comment = Comment.objects.get(id=comment_id)
    send_mail(
        subject=f'best MMORPG: новый комментарий на пост!',
        message=f'Доброго дня, {comment.post.person.username}, ! На Ваш пост есть новый комментарий\n',
         from_email='fedos.py@ya.ru',
        recipient_list=[comment.post.person.email],
    )


@shared_task
def comment_accept_send_email(comment_id):
    comment = Comment.objects.get(id=comment_id)
    print(comment.post.author.email)
    send_mail(
        subject=f'best MMORPG: Ваш комментарий принят!',
        message=f'Доброго дня, {comment.person}, Автор поста {comment.post.title} принял Ваш комментарий!\n',
        from_email='fedos.py@ya.ru',
        recipient_list=[comment.post.person.email],
    )
