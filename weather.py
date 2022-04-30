import requests

API_KEY = "4b8e54bac7126f02b5732c4a7b936905"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name:  ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperture = round(data["main"]["temp"]-273.15 , 2)
    country = data['sys']['country']
    min_temp = round(data['main']['temp_min']-273.15 , 2)
    max_temp = round(data['main']['temp_max']-273.15 , 2)
    sun_rise = data['sys']['sunrise']
    sun_set = data['sys']['sunset']
    print("country:" ,country)
    print("Weather:" , weather)
    print("Temperature:" ,temperture , "celsius")
    print("minimum temperature:" ,min_temp , "celsius")
    print("maximum temperature:" ,max_temp , "celsius")
    print("sunrise:" , sun_rise)
    print("sunset:" , sun_set)
    #print(data)
    
else:
    print("an error occurred.")