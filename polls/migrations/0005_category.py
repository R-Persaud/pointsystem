# Generated by Django 4.1.7 on 2023-05-30 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_rename_criteria1_responsibilities_criteria_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
            ],
        ),
    ]
