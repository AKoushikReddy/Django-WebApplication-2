from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserProfile
from django.forms import ModelForm


# Register Form inherits UserCreation Form, used in registration views

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name']

    def save(self, commit=True):
        # Calls the super class object and saves it
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['username']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            # Saves again with additional information
            user.save()

        return user


# ChangeForm inherits UserChangeForm, used to edit account information.

class ChangeForm(UserChangeForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['password', 'email', 'first_name', 'last_name']


# Profile Form : ModelFrom, Additional Information i.e. Custom Table in Database,
# Uses UserProfile model which is created when user is registered

class ProfileForm(ModelForm):
    # user is not an attribute here
    # We don't want the end user to change the user in the Model (profile model with One to One relation

    class Meta:
        model = UserProfile
        fields = ['shortbio', 'interests', 'image']
