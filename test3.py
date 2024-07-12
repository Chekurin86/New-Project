

import requests
import time


API_URL: str = 'https://api.telegram.org/bot'
API_CATS_URL: str = 'https://api.thecatapi.com/v1/images/search'
API_DOGS_URL: str = 'https://random.dog/woof.json'
API_FOXS_URL: str = 'https://randomfox.ca/floof/'
BOT_TOKEN: str = "7347541686:AAER4jOnrHGDZYCKwhplv62zb5IPU-25YFI"
ERROR_TEXT: str = 'Здесь должна была быть картинка с грязным бесчувственным животным :('

offset: int = -2
counter: int = 0
response: requests.Response
link: str


while counter < 100:
    print('attempt =', counter)
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            response = requests.get(API_DOGS_URL)
            if response.status_code == 200:
                link = response.json()['url']
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={link}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

    time.sleep(1)
    counter += 1

