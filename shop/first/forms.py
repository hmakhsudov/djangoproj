from django import forms


class OrderForm(forms.Form):
    name = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'css_input'}))
    number = forms.CharField(max_length=200)