import requests

params = {
    'apiKey': '262823828195400eb18143315231311',
    'city':'London'
}
url = f"https://api.weatherapi.com/v1/search.json?key={params['apiKey']}&q={params['city']}"

res = requests.get(url)
print(res.json())
