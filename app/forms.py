from django import forms
from django.forms import fields
from . models import blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class blog_form(forms.ModelForm):
    class Meta:
        model=blog
        fields="__all__"

        title=forms.CharField(widget=forms.TextInput({"Placeholder":"Enter your title"}))
        content=forms.CharField(widget=forms.TextInput({"Placeholder":"Write your content"}))

        date=forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}))


class signup_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
        username = forms.CharField(label='Name',max_length=200)
        email = forms.EmailField(max_length=200)
        password1 = forms.CharField(widget=forms.PasswordInput,label='Password')
        password2 = forms.CharField(widget=forms.PasswordInput,label='confirm Password')