# Generated by Django 4.2.5 on 2023-09-22 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_alter_task_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-updated']},
        ),
    ]
