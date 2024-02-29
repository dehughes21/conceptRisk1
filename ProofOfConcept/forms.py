from django.forms import ModelForm
from django import forms
from .models import Squirrel

class CreateForm(ModelForm):

    name = forms.TextInput()
    weight = forms.IntegerField()
    image = forms.ImageField()

    class Meta:
        model = Squirrel
        fields = ['name', 'weight', 'image']