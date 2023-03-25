import requests
api_key = "316022c480e74b7e9399ae73a007b075"
city = "Lucknow,india"

url = f"https://api.weatherbit.io/v2.0/current?city={city}&key={api_key}"
response = requests.get(url)

if response.status_code == 200:
    weather_data = response.json()
    print(f"Current temperature in {city}: {weather_data['data'][0]['temp']}°C")
    print(f"Conditions: {weather_data['data'][0]['weather']['description']}")
else:
    print("Error fetching weather data")