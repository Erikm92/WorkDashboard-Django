from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import userlinks, userheader



class userlinksForm(forms.ModelForm):
    class Meta:
        model= userlinks
        fields =['main', 'mainname', 'mainfavicon','table_id']
        widgets = {
            'main': forms.TextInput(attrs={'class':'form-control'}),
            'mainname': forms.TextInput(attrs={'class':'form-control'}),
            'mainfavicon': forms.TextInput(attrs={'class':'form-control'}),
            'table_id': forms.TextInput(attrs={'class':'form-control'})

        }
class userheaderForm(forms.ModelForm):
    class Meta:
        model= userheader
        fields =['header_id','header_name' ]
        widgets = {
            'header_id': forms.TextInput(attrs={'class':'form-control'}),
            'header_name': forms.TextInput(attrs={'class':'form-control'}),
            

        }
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
            )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()

        return user

class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = {
            'email',
            'first_name',
            'last_name',
            'password'
        }
        


