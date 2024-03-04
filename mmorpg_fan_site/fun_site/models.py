from django.db import models

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

class Person(models.Model):
    pass
class Post(models.Model):
    pass

class Comment(models.Model):
    pass