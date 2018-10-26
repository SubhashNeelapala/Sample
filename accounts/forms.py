from django import forms
from .models import *
class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Username'}))
    password = forms.CharField(max_length=60, widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': 'Password',}))

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)



my_default_errors = {
    'required': 'This field is required',
    'invalid': 'Enter a valid value'
}

class UserRegistrationForm(forms.ModelForm):
    username=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Username'}))
    first_name=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'First Name'}))
    last_name=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Last Name'}))
    mobile_number=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Mobile'}))
    age=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Age'}))
    email=forms.EmailField(max_length=25,widget=forms.EmailInput(attrs={'class':"form-control",'placeholder':"Email"}))
    gender=forms.ModelChoiceField(queryset=Gender.objects.all(), widget=forms.Select(attrs={'class':"form-control"}))
    department=forms.ModelChoiceField(queryset=Department.objects.all(),widget=forms.Select(attrs={'class':"form-control",'placeholder':"select"}))
    def __init__(self,*args,**kwargs):
        super(UserRegistrationForm,self).__init__(*args,**kwargs)
    class Meta:
        model=User
        exclude =("password", "date_joined")