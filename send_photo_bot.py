import requests
import random

CATS_API_URL = "https://api.thecatapi.com/v1/images/search"
DOGS_API_URL = "https://random.dog/woof.json"
FOXES_API_URL = "https://randomfox.ca/floof/"
CAPYBARA_API_URL = "https://api.capy.lol/v1/capybara?json=true"


def get_photo_url() -> str|None:
    match random.randint(1, 4):
        case 1:
            response = requests.get(CATS_API_URL)
            if response.status_code == 200:
                return response.json()[0]["url"]
        case 2:
            response = requests.get(DOGS_API_URL)
            if response.status_code == 200:
                return response.json()["url"]
        case 3:
            response = requests.get(FOXES_API_URL)
            if response.status_code == 200:
                return response.json()["link"]
        case 4:
            response = requests.get(CAPYBARA_API_URL)
            if response.status_code == 200:
                return response.json()["data"]["url"]


photo_url = get_photo_url()
print(photo_url)