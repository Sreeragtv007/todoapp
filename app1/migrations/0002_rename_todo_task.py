# Generated by Django 4.2.5 on 2023-09-20 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='todo',
            new_name='Task',
        ),
    ]