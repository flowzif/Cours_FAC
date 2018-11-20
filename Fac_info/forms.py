from django import forms

class ConnexionForm(forms.Form):
    username= forms.CharField(label="Nom d'utilisateur",max_length=30)
    paassword=forms.CharField(label="Mot de passe",widget=forms.PasswordInput)
    