from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100,required=True, widget=forms.TextInput(attrs={'placeholder': 'John', 'class': 'Input'}))
    last_name = forms.CharField(max_length=100,required=True, widget=forms.TextInput(attrs={'placeholder': 'Doe', 'class': 'Input'}))
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Johnyy', 'class': 'Input'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'john@example.com', 'class': 'Input'}))
    password1 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'Input'}))
    password2 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'Input'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']