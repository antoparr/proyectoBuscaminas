from django import forms

class tableForm(forms.Form):
    fila = forms.CharField(label='Fila:', max_length=15)
    columna = forms.CharField(label='Columna', max_length=12)