# Generated by Django 4.1.7 on 2023-06-26 02:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_login'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='login',
            new_name='loginModel',
        ),
    ]