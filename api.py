import datetime
from flask import Flask, request
from db import sqliteDb
import json
import pandas as pd
import numpy as np
import datetime
import pandas_ta as ta


app = Flask(__name__)


@app.route("/get-data", methods=['GET'])
def get_data():
    database = sqliteDb()
    currency = request.args.get('currency')
    timeframe = request.args.get('timeframe')
    indicator_name = request.args.get('indicator_name')
    indicator_period = request.args.get('indicator_period')
    candle = request.args.get('candle')
    response = database.getData(currency, timeframe)
    database.close()
    df = pd.DataFrame.from_records(response, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    if indicator_name == 'EMA':
        indicator = ta.ema(df['close'], length=int(indicator_period))
    elif indicator_name == 'RSI':
        indicator = ta.rsi(df['close'], length=int(indicator_period))
    indicator = indicator.fillna('undefined')
    dict = indicator.to_dict()
    result = {'open value': response[99-int(candle)][1],
              'high value': response[99-int(candle)][2],
              'low value': response[99-int(candle)][3],
              'close value': response[99-int(candle)][4],
              'timestamp': response[99-int(candle)][0],
               indicator_name:dict[99-int(candle)]}
    return json.dumps(result)


if __name__ == "__main__":
    app.run(port=8081)
