from django import forms
from . import models


class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", required=True, max_length=100)


class PersonForm(forms.ModelForm):
    class Meta:
        model = models.Person
        fields = ["your_name"]
