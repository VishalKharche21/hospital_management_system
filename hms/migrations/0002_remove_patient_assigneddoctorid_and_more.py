# Generated by Django 4.1.6 on 2023-02-09 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='assignedDoctorId',
        ),
        migrations.AddField(
            model_name='patient',
            name='assignedDoctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hms.doctor'),
        ),
    ]
