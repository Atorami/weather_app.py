from django.http import response
from django.shortcuts import render
from .forms import WeatherForm


def index(request):
    return render(request, 'index.html')


def get_info(request):
    if request.method == 'POST':
        form = WeatherForm(request.POST)

        if form.is_valid():
            city = form.cleaned_data['city']
            api_url = 'https://api.open-meteo.com/v1/forecast'
            weather_response = request.get(api_url, params={'location': city})
            response_data = weather_response.json()
            return render(request, 'index.html', {'form': form, 'weather_data': response_data})
        else:
            form = WeatherForm()
    return render('index.html', {'form': form})
