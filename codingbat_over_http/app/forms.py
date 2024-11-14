from django import forms

class FrontTimesForm(forms.Form):
    text = forms.CharField(label="Enter a string", max_length=100)
    n = forms.IntegerField(label="Number of copies", min_value=0)

class NoTeenSumsForm(forms.Form):
    a = forms.IntegerField(label="Enter first integer")
    b = forms.IntegerField(label="Enter second integer")
    c = forms.IntegerField(label="Enter third integer")

class XyzThereForm(forms.Form):
    text = forms.CharField(label="Enter a string", max_length=100)

class CenteredAverageForm(forms.Form):
    numbers = forms.CharField(label="Enter a list of integers (comma-separated)", max_length=200)