from django import forms

class AvailabilityForm(forms.Form):
    check_in = forms.DateTimeField(required=True, widget=forms.DateInput(attrs={"class" : "form-control"}))
    check_out = forms.DateTimeField(required=True, widget=forms.DateInput(attrs={"class" : "form-control"}))
    