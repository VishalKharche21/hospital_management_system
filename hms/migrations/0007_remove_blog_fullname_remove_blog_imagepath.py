# Generated by Django 4.1.6 on 2023-02-15 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0006_blog_fullname_blog_imagepath'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='fullname',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='imagepath',
        ),
    ]