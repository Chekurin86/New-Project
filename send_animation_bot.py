

import requests
import time


API_URL: str = 'https://api.telegram.org/bot'
URL: str = 'https://yesno.wtf/api'
BOT_TOKEN = "7347541686:AAER4jOnrHGDZYCKwhplv62zb5IPU-25YFI"
ERROR_TEXT = 'Здесь должна была быть картинка с животным :('

offset: int = -2
counter: int = 0
cat_response: requests.Response
link: str


while counter < 100:
    print('attempt =', counter)
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            response = requests.get(URL)
            if response.status_code == 200:
                link = response.json()["image"]
                requests.get(f'{API_URL}{BOT_TOKEN}/sendAnimation?chat_id={chat_id}&animation={link}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')



    time.sleep(1)
    counter += 1