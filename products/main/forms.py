
from django import forms


class SearchForm(forms.Form):
    """Stockreading form"""

    stockreading = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'ex: 1231231231231'}))
    

class AddInfos(forms.Form):
    """New product form"""

    name = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'ex: coca-cola'}))
    description = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'ex: soda - bootle'}))
    stockreading = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder': 'ex: 1231231231231'}))
    expires = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD', 'required': 'required'}))