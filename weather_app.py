
#importing modules
import os
import emoji
import requests
import json
from datetime import datetime
from time import sleep

#description of project
print("Hello Folks ..This is my first weather app")
sleep(0.5)

print("Here, you can find weather in your city!")
sleep(1)

#access API key
weather_api_key = os.environ["weather_apikeys"]

#location from user
location = input("Enter location: ")

#URL
api_url = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+ weather_api_key

#HTTP request
result=requests.get(api_url)


#convert ('result'json) into dictionary:--
data=result.json()             #data is in dictionary form


if(data.get('cod')=="404"):
    print(emoji.emojize(":snake:"),end=" ")
    print(emoji.emojize(":snake:"),end=" ")
    print("\U0001F923", end=" ")
    print(emoji.emojize(":snake:"),end=" ")
    print(emoji.emojize(":snake:"),end=" ")


    print(f"\nEntered city is not valid or Check Your spelling of entered city: {location}\n")
    exit()
else:
    temp= data.get("main").get('temp')-273.15
    lon = data.get("coord").get('lon')
    lat = data.get("coord").get('lat')
    pressure = data.get("main").get('pressure')
    humidity = data.get("main").get('humidity')
    speed = data.get('wind').get('speed')
    description = data.get('weather')[0].get("description")
    date_time = datetime.now().strftime("%D %M %Y | %H:%M:%S %p")
print("||----------------------------------------------------------------||")
print(f"  Location: {location} ||||  Date&Time : {date_time}")
sleep(2)
print(f"  Scenerio of {location}: {description}")
sleep(2)
print(f"  Temperature of {location}: {temp}")
sleep(2)
print(f"  Longitude of {location}: {lon}")
sleep(2)
print(f"  Latitude of {location} : {lat}")
sleep(2)
print(f"  Pressure of {location}: {pressure}")
sleep(2)
print(f"  Wind Speed of {location} : {speed}")
sleep(2)
print("||----------------------------------------------------------------||")
sleep(2)
print("Thank You Roop & Aman!!")
