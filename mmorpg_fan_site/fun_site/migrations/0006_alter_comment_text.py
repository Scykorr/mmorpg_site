# Generated by Django 5.0.3 on 2024-03-10 09:02

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fun_site', '0005_alter_category_category_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
