from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    tank = 'TNK'
    heal = 'HL'
    dd = 'DD'
    merchant = 'MRCHNT'
    guildmaster = 'GLDMSTR'
    questgiver = 'QSTGVR'
    blacksmith = 'BLCKSMTH'
    tanner = 'TNNR'
    potionmaster = 'PTNMSTR'
    wizard = 'WZRD'

    TYPES = [
        ('TNK', 'Танк'),
        ('HL', 'Хил'),
        ('DD', 'ДД'),
        ('MRCHNT', 'Торговец'),
        ('GLDMSTR', 'Гильдмастер'),
        ('QSTGVR', 'Квестгивер'),
        ('BLCKSMTH', 'Кузнец'),
        ('TNNR', 'Кожевник'),
        ('PTNMSTR', 'Зельевар'),
        ('WZRD', 'Мастер заклинаний')

    ]
    category = models.CharField(max_length=8, choices=TYPES, default=dd)

    def __str__(self) -> str:
        return self.get_category_display()


class Person(models.Model):
    person = models.OneToOneField(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.person.username


class Post(models.Model):
    text = RichTextUploadingField()
    create_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, default='***')
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title.title()}: {self.text[:15]}...'

    def preview(self):
        return f'{self.text[:124]}...'


class Comment(models.Model):
    text = models.TextField()
    is_fix = models.BooleanField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
