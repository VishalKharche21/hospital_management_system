# Generated by Django 4.1.6 on 2023-02-14 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0003_blogimages_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='doctor',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='is_draft',
            field=models.BooleanField(default=False),
        ),
    ]
