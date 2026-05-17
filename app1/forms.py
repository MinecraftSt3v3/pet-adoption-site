from django import forms
from django.contrib.auth.models import User
from app1.models import userPost
from django.core.validators import RegexValidator

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class userPostForm(forms.ModelForm):
    description = forms.CharField(widget=forms.TextInput(attrs={'size': '35'}))
    itemPhoto = forms.ImageField(required=True)
    class Meta():
        model = userPost
        fields = ('description','category', 'itemPhoto') 

class JoinForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150,
        validators=[
            RegexValidator(
                regex=r'^[\w.@+-]+$',
                message='Username may contain only letters, digits, and @/./+/-/_ characters.'
            )
        ]
    )
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(required=True)

    class Meta():
        model = User
        fields = ('username', 'email', 'password')