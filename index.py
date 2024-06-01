import requests
import json

url = "http://api.alquran.cloud/v1/quran/en.asad"


response = requests.request("GET", url)



for i in range(len(response.json()['data']['surahs'])):
    for j in range(len(response.json()['data']['surahs'][i]['ayahs'])):
        with open('quran.txt', 'a') as quran:
            quran.write(f"{response.json()['data']['surahs'][i]['ayahs'][j]['text']}\n")
    





