import requests

api_url = "https://api.telegram.org/bot7347541686:AAER4jOnrHGDZYCKwhplv62zb5IPU-25YFI/getUpdates"

response = requests.get(api_url)

if response.status_code == 200:
    print(response.json())
else:
    print(response.status_code)