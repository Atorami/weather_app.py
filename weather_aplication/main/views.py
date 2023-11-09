from django.http import response
from django.shortcuts import render
import requests


def index(request):
    api_key = 'bae0f65dddcd53bf9084c40863033a8f'
    if request.method == 'POST':
        city = request.POST['location']
        api_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
        response_data = requests.get(api_url.format(city, api_key)).json()
        print(response_data)
        weather_data = {
            'temp': response_data['main']['temp'],
            'temp_min': response_data['main']['temp_min'],
            'temp_max': response_data['main']['temp_max'],
            'pressure': response_data['main']['pressure'],
            'humidity': response_data['main']['humidity'],
            'icon_nr': response_data['weather'][0]['icon'],
        }
        print(weather_data)
        return render(request, 'index.html', {'response_data': weather_data})
    else:
        return render(request, 'index.html')
