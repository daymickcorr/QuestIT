# Generated by Django 3.2.12 on 2022-04-13 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0012_character_defaultcharacter_defaultexit_defaultobject_defaultroom_object'),
        ('quest', '0009_alter_quest_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='author',
            field=models.ForeignKey(limit_choices_to={'db_typeclass_path': 'typeclasses.characters.Character'}, on_delete=django.db.models.deletion.DO_NOTHING, to='objects.objectdb'),
        ),
    ]
