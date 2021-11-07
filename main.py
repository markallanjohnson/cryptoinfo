from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'25',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  #'X-CMC_PRO_API_KEY': key,
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  data = data['data']
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

crypto_info = {}
total_market_cap = 0

for coin in data:
    name = coin['name']
    cap = int(coin['quote']['USD']['market_cap'])
    crypto_info[name] = {'market_cap': cap}
    total_market_cap += cap

# cache data
# when ran again, compare values, notify if new entrant. detect if
# coin climbs a tier. don't get confused if a coin that was previously
# in the top 25 makes it back again.
