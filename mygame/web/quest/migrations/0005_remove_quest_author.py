# Generated by Django 3.2.12 on 2022-04-13 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quest', '0004_alter_quest_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quest',
            name='author',
        ),
    ]
