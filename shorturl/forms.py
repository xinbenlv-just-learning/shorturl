from django.forms import ModelForm
from django import forms
from django.forms import fields, models, formsets, widgets
from shorturl.models import Sue

class SueForm(models.ModelForm):
    
    class Meta:
        model = Sue

        exclude = ('short','owner', 'count', 'created_date')
