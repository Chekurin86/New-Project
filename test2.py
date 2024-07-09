import requests
import pprint

api_url = "http://api.telegram.org/bot7347541686:AAER4jOnrHGDZYCKwhplv62zb5IPU-25YFI/sendMessage?chat_id=6991696753&text=Привет. дружище!!!"

response = requests.get(api_url)

if response.status_code == 200:
    pprint.pprint(response.text)

else:
    print(requests.status_code)