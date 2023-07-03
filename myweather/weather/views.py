from django.shortcuts import render
import datetime as dt
import requests

from django.http import HttpResponse 
from django.urls import reverse


def index(request):
    context = {
        'temp_city': temp_city,
        'temp_celcius': temp_celcius,
        'temp_kelvin': temp_kelvin,
        'temp_humiditiy': temp_humiditiy,
        'temp_status': temp_status,
        'temp_lat': temp_lat,
        'temp_lon' : temp_lon,
    }
    return render(request, 'template_app/index.html', context)



base_url = "http://api.openweathermap.org/data/2.5/weather?"
#enter your api in api_key.txt
api_key =  open('template/template_app/api_key.txt','r').read()

city = "İstanbul"

url = base_url + "appid=" + api_key + "&q=" + city

response = requests.get(url).json()

def kelvin_to_celcius(kelvin):
    celcius = kelvin - 272.15
    return celcius


#city
temp_city = response['name']

#celcius
temp_kelvin  = response['main']['temp']
temp_celcius = kelvin_to_celcius(temp_kelvin)
temp_celcius = round(temp_celcius)

#humidity
temp_humiditiy = response['main']['humidity']
temp_humiditiy = str(temp_humiditiy) + "%"

#temp status
temp_status  = response['weather'][0]['description']

#lat(enlem) and lon(boylam) 
temp_lat = response['coord']['lat']
temp_lon = response['coord']['lon']


print(temp_lat)