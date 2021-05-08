## Установка
Требуемые пакеты: Flask, pandas-ta, requests.
## Запуск
Запупсить filldb.py. Этот скрипт обновит данные в бд по свечам.
```
$py filldb.py
```
Запускаем flask-сервер:
```
$py api.py
```
## Обращение к API
Пример GET-запроса:

http://127.0.0.1:8081/get-data?currency=XLMUSDT&timeframe=1d&indicator_name=RSI&indicator_period=10&candle=3

обозначение параметров:

currency - назвние валютной пары

timeframe - таймфрейм // 1d или 1h

indicator_name - название нужного индикатора// RSI или EMA

indicator_period - период заданного индикатора

candle - номер свечи

