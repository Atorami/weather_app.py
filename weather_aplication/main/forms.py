from django import forms


class WeatherForm(forms.Form):
    city = forms.CharField(label='Enter Location', max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Enter a city'}))
