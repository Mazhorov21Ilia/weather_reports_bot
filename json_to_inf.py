import json

with open('forecast.json', 'r') as file:
    data = json.load(file)
    for i in data["forecast"]["forecastday"]:
        print(f"{i["date"]} - {i["day"]["condition"]["text"]}")