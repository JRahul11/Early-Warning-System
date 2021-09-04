from django import forms
from .models import ProfileModel


class NewProfileForm(forms.ModelForm):
    name = forms.CharField(label="Name", widget=forms.TextInput(
        attrs={'autofocus': 'autofocus'}), required=True)
    dob = forms.DateInput(attrs={'type': 'date'})
    gender = forms.ChoiceField(label="Gender", choices=[(
        "Male", "Male"), ("Female", "Female"), ("Other", "Other")])
    phone = forms.IntegerField(label="Phone")

    class Meta:
        model = ProfileModel
        fields = ()


class NewHomePageForm(forms.Form):
    city = forms.CharField(widget=forms.TextInput(attrs={
                           'class': 'form-control', 'id': 'formGroupExampleInput', 'placeholder': 'Eg. Mumbai', 'style': 'text-align: center;', 'name': 'city', 'type': 'text', 'required': 'True'}))
    date = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'date', 'id': 'date', 'name': 'date', 'required': 'True'}))
