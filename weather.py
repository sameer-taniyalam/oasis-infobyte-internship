

import requests
import json
country=input("enter the country:\n")
city=input("Enter city name:\n")
api_key="778a2328107c4711b30a173c0251fc6f"
full_url=f"http://api.weatherbit.io/v2.0/current?&key={api_key}&city={city}&country={country}"
response=requests.get(full_url)
if response.status_code==200:
  weather_data=response.json()
  first=weather_data['data']
  name=first[0]
  clouds=name['clouds']
  temprature=name['temp']
  wind_speed=name['wind_spd']
  weather_desc=name['weather']['description']
  print(f"Weather details in{city}:")
  print("Area covered by clouds:",clouds)
  print(f"The temprature is {temprature} \u00b0C")
  print(f"Thw wind spped is {wind_speed}m/s")
  print("The weather has",'',weather_desc)
else:
  print("Failed to fetch weather data")











 











