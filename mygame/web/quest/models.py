from pickle import FALSE
from sqlite3 import Date
from django.db import models
from evennia.objects.models import ObjectDB
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Quest(models.Model):
    title = models.CharField(max_length=255)
    note = models.TextField(blank=True)
    difficulty = models.IntegerField(
        default=1,
        blank=False, 
        validators=[MaxValueValidator(10)]
        )
    due_date = models.DateField(
        blank=True, 
        validators=[MinValueValidator(Date.today())]
        )
    #author relation
    author = models.ForeignKey(
        ObjectDB, 
        on_delete=models.CASCADE,
        limit_choices_to={'db_typeclass_path' : 'typeclasses.characters.Character' },
        related_name='+', #no relations from author to quest only from quest to author
        blank=False,
        default=1,
        )
    #characters that have accepted the quest 
    hero = models.ManyToManyField(
        ObjectDB, 
        limit_choices_to={'db_typeclass_path' : 'typeclasses.characters.Character' },
        blank=True,
        )
    #reward relation

    #permitted characters to access this quest

    #changes display
    #def __str__(self):
    #    return self.title;