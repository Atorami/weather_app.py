from django.http import response
from django.shortcuts import render
import requests


def index(request):
    api_key = 'bae0f65dddcd53bf9084c40863033a8f'
    if request.method == 'POST':
        city = request.POST['location']
        api_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
        response_data = requests.get(api_url.format(city, api_key)).json()

        if response_data['cod'] == 200:
            weather_data = {
                'city': response_data['name'],
                'temp': round(response_data['main']['temp']-273.15),
                'temp_min': round(response_data['main']['temp_min']-273.15),
                'temp_max': round(response_data['main']['temp_max']-273.15),
                'pressure': response_data['main']['pressure'],
                'humidity': response_data['main']['humidity'],
                'icon_nr': response_data['weather'][0]['icon'],
            }

            return render(request, 'index.html', {'response_data': weather_data})
        else:
            err_msg = response_data['message'].capitalize()
            return render(request, 'index.html', {'error': err_msg})
    else:
        return render(request, 'index.html')
