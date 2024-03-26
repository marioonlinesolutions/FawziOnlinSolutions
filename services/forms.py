from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.forms.widgets import TextInput,PasswordInput


class Registration(UserCreationForm):
      
      class Meta:
            model = User
            fields = ['username','email','password1','password2']

class loginform(AuthenticationForm):

      username = forms.CharField(widget=TextInput())
      password = forms.CharField(widget=PasswordInput())


class Sendingemail(forms.Form):

      subject = forms.CharField(max_length=100)      
      message = forms.CharField(widget=forms.Textarea)

