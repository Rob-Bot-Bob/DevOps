import requests
import json
baseUrl = 'https://api.upcitemdb.com/prod/trial/lookup'
parameters = {'upc': '073366118238'}
response = requests.get(baseUrl, params=parameters)
print(response.url)
content = response.content
info = json.loads(content)
item = info['items']
itemInfo = item[0]
title = itemInfo['title']
brand = itemInfo['brand']
print(title)
print(brand)

#apikeys sometimes keys will be needed in order to use the API
#import requests
#baseUrl = 'http://api.openweathermap.org/data/2.5/forecast'
#parameters = {'APPID': 'key','q':'Seattle,US'}
#response = requests.get(baseUrl, params=parameters)
#print(response.content)