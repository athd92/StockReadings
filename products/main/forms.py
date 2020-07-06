
from django import forms


class SearchForm(forms.Form):
    """Stockreading form"""

    stockreading = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'ex: 1231231231231'}))
    
