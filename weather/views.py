from django.shortcuts import render
import requests 
from .models import City
from .forms import CityForm

def index(request):
    appid = '8fbbac47ea18c4d4dd5967f9c14bef36'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()
    form = CityForm()
    cities = City.objects.all()
    all_cities = []
    for city in cities :
        res = requests.get(url.format(city.name)).json() #функция json конвертирует данные в словарь
        city_info = {
            'city':city.name,
            'temp':res['main']['temp'],
            'icon':res['weather'][0]['icon'],
            'feels_like':res['main']['feels_like'],
            'wind':res['wind']['speed']
        }
        all_cities.append(city_info)
    context = {'all_info':all_cities, 'form':form}
    return render(request, 'weather/index.html',context)
