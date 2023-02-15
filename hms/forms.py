from django import forms
from django.contrib.auth.models import User
from .models import *
from django.core import validators
from django.core.validators import RegexValidator
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm,PasswordChangeForm


class DoctorUserForm(UserCreationForm):
    password2=forms.CharField(label='Confirm Password (Again)',min_length=6, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password1=forms.CharField(label='Password',min_length=6, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(label='First name',max_length=21,min_length=2,validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',message='Only letters is allowed')])
    last_name=forms.CharField(label='Last name',max_length=21,min_length=2,validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',message='Only letters is allowed')])
    email=forms.CharField(label='Email',max_length=100,validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$',message='Please Enter Valid Mail id')])
    username=forms.CharField(max_length=100,min_length=5)

    def clean_username(self):
        valusername=self.cleaned_data['username']
        if User.objects.filter(username=valusername).exists():
            raise forms.ValidationError('That username is taken. Try another.')
        return valusername

    def clean_password2(self):
        valpass1=self.cleaned_data['password1']
        valpass2=self.cleaned_data['password2']
        if valpass1 != valpass2:
            raise forms.ValidationError('Those passwords didnt match. Try again.')
        return valpass1
            

    class Meta:
        model= User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email'}
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }


class DoctorForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields=['address','mobile','department','profile_pic']

class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control mb-0','placeholder':'*******'}))
      



class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields=['address','mobile','symptoms','profile_pic','assignedDoctor',]
