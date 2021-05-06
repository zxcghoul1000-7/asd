from binance_api import Binance
import sqlite3
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
db.clear()
for currency in pattern[0]:
    for interval in pattern[1]:
        responses = api.call_api(**{'command': 'klines', 'symbol': currency, 'interval': interval, 'limit': 100})
        responses=responses[::-1]
        for record in responses:
            db.addToDb(int(record[0]),float(record[1]),float(record[2]),float(record[3]),float(record[4]),currency,interval)
        db.close()
        print('finished')