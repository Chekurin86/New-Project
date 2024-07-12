import requests
import pprint

api_url = 'https://yesno.wtf/api'

response = requests.get(api_url)

if response.status_code == 200:
    pprint.pprint(response.json())

else:
    print(requests.status_code)