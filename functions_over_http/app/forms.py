from django import forms

class HeyYouForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)

class AgeInForm(forms.Form):
    end_year = forms.IntegerField(label="End Year")
    birth_year = forms.IntegerField(label="Birth Year")

class OrderForm(forms.Form):
    burgers = forms.IntegerField(label="Burgers", min_value=0)
    fries = forms.IntegerField(label="Fries", min_value=0)
    drinks = forms.IntegerField(label="Drinks", min_value=0)