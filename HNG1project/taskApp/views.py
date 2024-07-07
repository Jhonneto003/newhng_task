from django.shortcuts import render

from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import requests
from django.conf import settings


# Create your views here.
class TaskView(View):
    def get(self,request):
        #get the visitor name from query parameters
        visitor_name= request.GET.get('visitor_name',"Guest")

        #get the client's IP address
        client_ip= request.META.get('HTTP_X_FORWARDED_FOR')
        if client_ip:
            # 'HTTP_X_FORWARDED_FOR'  header can contain multiple IPs, so we take the first IP address
            client_ip = client_ip.split(',')[0].strip()
        
        else:
            client_ip= request.META.get('REMOTE_ADDR')

        
        try:
            #get location based on the ip using openweathermap service
            location_response = requests.get(f'https://ip-api.com//json/{client_ip}')
            location_data = location_response.json()
            location = location_data.get('location', 'Unknown')

            #get weather data
            # weatherapi_key = settings.WEATHER_API_KEY
            WEATHER_API_KEY= '1b1a89458dfb921532441cf9a48abb43'
            weather_response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={WEATHER_API_KEY}&units=metric')
            weather_data = weather_response.json()
            temperature = weather_data['main']['temp']

            response_data = {
                'client_ip' : client_ip,
                'location'  : location,
                'greeting'  : f'Hello, {visitor_name}! The temperature is {temperature} degree Celsius in {location}'

            }

        except Exception as e:
            response_data = {
                'error': str(e)
            }
        return JsonResponse(response_data)




