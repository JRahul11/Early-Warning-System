from django import forms


class NewHomePageForm(forms.Form):
    city = forms.CharField(widget=forms.TextInput(attrs={
                           'class': 'form-control', 'id': 'formGroupExampleInput', 'placeholder': 'Eg. Mumbai', 'style': 'text-align: center;', 'name': 'city', 'type': 'text', 'required': 'True'}))
    date = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'date', 'id': 'date', 'name': 'date', 'required': 'True'}))
