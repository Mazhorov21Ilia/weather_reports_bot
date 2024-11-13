import requests
import weatherapi 
import json
import datetime

configuration = weatherapi.Configuration()
configuration.api_key['key'] = '6dd795ec5ecd4c629c0211009241311'

api_instance = weatherapi.APIsApi(weatherapi.ApiClient(configuration))
q = 'Moscow'
days = 14
dt = datetime.date.today()
lang = 'ru'

with open("forecast.json", "w") as file:
    try:
        api_response = api_instance.forecast_weather(q, lang=lang, days=days, aqi='no')
        json.dump(api_response, file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(e)