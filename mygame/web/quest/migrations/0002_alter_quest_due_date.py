# Generated by Django 3.2.12 on 2022-04-13 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='due_date',
            field=models.DateField(),
        ),
    ]
