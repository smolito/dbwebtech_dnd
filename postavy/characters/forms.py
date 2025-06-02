# characters/forms.py

from django import forms
from .models import Postava

class PostavaForm(forms.ModelForm):
    class Meta:
        model = Postava
        fields = ['jmeno', 'rasa', 'trida', 'uroven', 'sila', 'zivotopis', 'je_aktivni']
        # widgety ~ pro změny výchoho vzhledu polí, můžu použít třídy z Bootstrapu
        widgets = {
            'jmeno': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Jméno postavy'}),
            'rasa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Např. Člověk, Elf'}),
            'trida': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Např. Válečník, Kouzelník'}),
            'uroven': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'max': '20'}),
            'sila': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'max': '30'}),
            'zivotopis': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Krátký popis postavy...'}),
            'je_aktivni': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        # labels nebo texty nápovědy (help_texts)
        # pokud se liší od těch v modelu - více user-friendly ?
        labels = {
            'jmeno': 'Jméno Postavy',
            'je_aktivni': 'Je postava aktivní?'
        }
        help_texts = {
            'sila': 'Zadejte hodnotu síly mezi 1 a 20 (hard cap == 30, nepovinné).',
        }

    # vlastní validace pro formulář
    # def clean_jmeno(self):
    #     jmeno = self.cleaned_data.get('jmeno')
    #     if len(jmeno) < 2:
    #         raise forms.ValidationError("Jméno musí mít alespoň 2 znaky.")
    #     return jmeno