# Generated by Django 4.1.7 on 2023-09-22 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_task_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='date',
        ),
    ]
