# Generated by Django 5.0.3 on 2024-03-10 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fun_site', '0007_alter_comment_is_fix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(),
        ),
    ]