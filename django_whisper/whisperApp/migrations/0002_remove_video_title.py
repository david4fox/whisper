# Generated by Django 4.2.7 on 2023-11-14 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whisperApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='title',
        ),
    ]