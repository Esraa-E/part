from django import forms


class Wow(forms.Form):
    x = forms.CharField(label='Enter your prefered message: ',min_length=5)