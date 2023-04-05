from django import forms
from .models import UserEXT
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate




class RegisterForm(UserCreationForm):
    regno=forms.CharField(max_length=9)

    class Meta:
        model=UserEXT
        fields=('regno','password1','password2')

class LoginForm(forms.ModelForm):
    password=forms.CharField(label="Password",widget=forms.PasswordInput)
    class Meta:
        model=UserEXT
        fields=('regno','password')
    
    def clean(self):
        regno=self.cleaned_data['regno']
        password=self.cleaned_data['password']
        if (not(authenticate(regno=regno,password=password))):
            raise forms.ValidationError("Invalid RegNo/Password")
