from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AvailabilityForm(forms.Form):
    check_in = forms.DateTimeField(required=True, widget=forms.DateInput(attrs={"class" : "form-control"}))
    check_out = forms.DateTimeField(required=True, widget=forms.DateInput(attrs={"class" : "form-control"}))


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]