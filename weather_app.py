import requests

api_key = "5351d46c4f2cdfaa907c77aaeb4c0479"

city = input("Enter your city: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = round((data['main']['temp'] - 273.15) * 1.8 + 32)
    desc = data['weather'][0]['description']
    print(f'Temperature: {temp} F')
    print(f'Description: {desc}')
else:
    print('Error fetching weather data')

    