# Generated by Django 4.1.6 on 2023-02-14 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0004_alter_blog_doctor_alter_blog_is_draft'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='is_draft',
            field=models.CharField(default='No', max_length=5),
        ),
    ]