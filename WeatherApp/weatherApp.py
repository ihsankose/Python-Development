"""
    This app uses weatherapi.com to get weather information about a selected city.
"""
import json
import requests
MY_API_KEY = "e8c585e878d445ca9f800418232011"

print("Welcome to Weather App")

selectedCity = input("Please enter the city: ")

r = requests.get(
    f"http://api.weatherapi.com/v1/current.json?key={MY_API_KEY}&q={selectedCity}", timeout=5)

# For Debugging
# print(r.status_code)

# Weather app returns answer in json format.
r_json = json.loads(r.text)

varLocationName = r_json['location']['name']
varLocationCountry = r_json['location']['country']
varTemperature = r_json['current']['temp_c']
varHumidity = r_json['current']['humidity']
varComment = r_json['current']['condition']['text']


print(f'Weather Status for {varLocationName}/{varLocationCountry}')
print(f'Temperature: {varTemperature}C')
print(f'Humidity: {varHumidity}')
print(f'Comment: {varComment}')
