from django import forms
from django.forms import ModelForm
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['Medidor', 'Coordenadas', 'important']
        widgets = {
            'Medidor': forms.TextInput(attrs={'placeholder': 'No. Medidor'}),
            'Coordenadas': forms.TextInput(attrs={'placeholder': 'Ejemplo: -70.6970300, 19.4517000'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Medidor'].widget.attrs.update({'class': 'form-control mb-3'})
        self.fields['Coordenadas'].widget.attrs.update({'class': 'form-control mb-3'})

    important = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
