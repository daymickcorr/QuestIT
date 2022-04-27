from django import forms

class CharacterCreate(forms.Form):
    name = forms.CharField(label='Character name', max_length=80)