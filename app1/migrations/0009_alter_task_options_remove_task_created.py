# Generated by Django 4.2.5 on 2023-09-22 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_alter_task_options_remove_task_updated'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={},
        ),
        migrations.RemoveField(
            model_name='task',
            name='created',
        ),
    ]
