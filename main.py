import requests
from requests import Session
import secret
from pprint import pprint
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': secret.API_KEY,
}

r = requests.get(url, headers=headers)


class CMC:
    def __init__(self, token) -> None:
        self.apiurl = 'https://pro-api.coinmarketcap.com'
        self.headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': token}
        self.session = Session()
        self.session.headers.update(self.headers)

    def getAllCoins(self):
        url = self.apiurl + '/v1/cryptocurrency/map'
        r = self.session.get(url, headers=self.headers)
        data = r.json()['data']
        return data
        
    def getPrice(self, symbol):
        url = url = self.apiurl + '/v2/cryptocurrency/quotes/latest'
        parameters = {'symbol': symbol}
        r = self.session.get(url, params=parameters)
        data = r.json()['data']
        return data

cmc = CMC(secret.API_KEY)

with open('res.json', 'w') as file_object:
    json.dump(cmc.getAllCoins(), file_object)

# pprint(cmc.getPrice('KISHU'))