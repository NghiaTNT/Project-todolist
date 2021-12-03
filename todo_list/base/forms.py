"""from django import forms
from django.forms import widgets
from .models import Task

class AddTask(forms.ModelForm):

    class Meta:
        model = Task
        field = ('name', 'complete', 'due_date', 'project', 'label')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'complete': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control'}),
            'project': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'label':forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
        """
