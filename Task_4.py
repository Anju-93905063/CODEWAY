import requests

api_key='12388dfa4bb05d448e80a7900b3d3247'
city=input("enter city:")
base_url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}"
params = {'q': city, 'appid': api_key, 'units': 'metric'}

response = requests.get(base_url, params=params)
data = response.json()

if data['cod'] == 200:
    weather = data['weather'][0]['description']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']

    print(f"Weather in {city}: {weather}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
else:
    print("City not found. Please check the city name and try again.")
