from binance_api import Binance
import datetime
import json
from db import sqliteDb
api = Binance('AMWNxQ9DJ7t7ZKEAR8qT5boPYrdUIQHXUXBb7BgGb4fgKP53yK0YXaG9XPPkrJXU', 'tSr4OaBiH0IXqXUNvVzsSRXyYpG314a03Yhltx9NQa9ok6M9h96YJwnu5BDMYGoa')
pattern = [["ETHUSDT",
            "LTCUSDT",
            "XLMUSDT",
            "XMRUSDT",
            "XEMUSDT"
            ],
           ['1h', '1d']]
db = sqliteDb()
print('recording to db...   '+datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
for currency in pattern[0]:
    for interval in pattern[1]:
        responses = api.call_api(**{'command': 'klines', 'symbol': currency, 'interval': interval, 'limit': 100})
        db.addToDb(currency,interval,json.dumps(responses))

db.close()
print('finished   '+datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))