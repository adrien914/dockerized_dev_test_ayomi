from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
#Formulaire d'inscription
#champs : username, email, mdp, confirmation mdp
class RegForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class UsernameUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
        
class EmailUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['email']

class PasswordUpdateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['password']
