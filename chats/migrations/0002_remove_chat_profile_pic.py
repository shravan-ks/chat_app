# Generated by Django 3.0 on 2019-12-14 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='profile_pic',
        ),
    ]
