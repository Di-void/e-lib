from django import forms

class SearchForm(forms.Form):
     title = forms.CharField(label='Search', max_length=100)