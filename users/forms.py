from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    def __init__(self, *args, **kwargs):
        super(SignUpForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'type':'text', 'placeholder':'Username', 'id':'username', 'name':'username', 'class' : 'form-control'})
        self.fields['email'].widget = forms.EmailInput(attrs={'type':'email','placeholder':'Email','id':'email','name':'email','class':'form-control'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'type':'password', 'placeholder':'Password....', 'id':'password1', 'name':'password1', 'class' : 'form-control'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'type':'password', 'placeholder':'Confirm Password.....', 'id':'password2', 'name':'password2', 'class' : 'form-control'})

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'type':'text','placeholder':'Username','id':'username','class':'form-control','name':'username'})
        self.fields['email'].widget = forms.EmailInput(attrs={'type':'email','placeholder':'Email','id':'email','name':'email','class':'form-control'})


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address','phone','image']

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['address'].widget = forms.TextInput(attrs={'type':'text','placeholder':'Address','name':'address','id':'address','class':'form-control'})
        self.fields['phone'].widget = forms.NumberInput(attrs={'type':'number','id':'phone','name':'phone','placeholder':'Phone Number','class':'form-control'})
        self.fields['image'].widget = forms.FileInput(attrs={'type':'file','class':'form-control-file'})