import requests
import json
import pyttsx3

while True:
    city = input("Enter city: \n")

    if city == "exit":
        break

    url = f"https://api.weatherapi.com/v1/current.json?key=78642129ffd74751a96200533242303&q={city}"

    response = requests.get(url)

    print(response.text)

    data = json.loads(response.text)
    
    # Add what you want to print for example temperature and other details
    print(data["current"]["temp_c"])
    print(data["current"]["condition"]["text"])
    print(data["location"]["name"])
    print(data["location"]["region"])
    print(data["location"]["country"])
    print(data["location"]["localtime"])

    #Add what you want to speak
    engine = pyttsx3.init()
    engine.say(data["current"]["temp_c"])
    engine.say(data["current"]["condition"]["text"])
    engine.say(data["location"]["name"])
    engine.say(data["location"]["region"])
    engine.say(data["location"]["country"])
    engine.say(data["location"]["localtime"])
    engine.runAndWait()

    print("Done")

# Add your api key SOURCE
    # https://www.weatherapi.com/my/fields.aspx ### To get free api key use this url
    # https://api.weatherapi.com/v1/current.json?key=78642129ffd74751a96200533242303&q=sahiwal  ## TO  create 
    # the real time weather APP url use this url make change your key and city.