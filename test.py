import requests
from bs4 import BeautifulSoup
import json

url = "https://dentalia.com/"

response = requests.get(url)
print(response)
soup = BeautifulSoup(response.content, "html.parser")
print(soup)


locations = []

# Здесь необходимо написать код для парсинга информации о локациях с сайта



# Пример добавления локации в список
location = {
    "name": "Название локации",
    "address": "Адрес",
    "coordinates": {"latitude": 0.0, "longitude": 0.0},
    "phones": ["Телефон 1", "Телефон 2"],
    "working_hours": {
        "Понедельник": "10:00 - 18:00",
        "Вторник": "10:00 - 18:00",
        # ...
    },
}
locations.append(location)

# Сохранение в JSON файл
with open("dentalia_locations.json", "w") as json_file:
    json.dump(locations, json_file, ensure_ascii=False, indent=4)