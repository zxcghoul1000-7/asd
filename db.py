import sqlite3
import datetime
import json
from time import time


class sqliteDb:
    def __init__(self):
        self.connection = sqlite3.connect('source_data.db')
        print("connected to db")

    def close(self, log=True):
        self.connection.close()
        if log == True:
            print("db is closed    "+datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))

    def clear(self, log=True):
        cursor = self.connection.cursor()
        cursor.executescript('''DELETE FROM data2;
                             VACUUM;''')
        if log == True:
            print('db cleared    '+datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
        self.connection.commit()
        cursor.close()

    def addToDb(self, currency, timeframe, json, log=True):
        cursor = self.connection.cursor()
        cursor.execute('''SELECT * FROM data2 WHERE currency=? AND timeframe=?;''', (currency, timeframe))
        records = cursor.fetchall()
        if len(records) == 0:
            cursor.execute('''INSERT INTO data2 (currency,timeframe,json) 
                              VALUES (?,?,?);''', (currency, timeframe, json))
            if log == True:
                print('recorded successfully   '+datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
        else:
            cursor.execute('''UPDATE data2
                              SET json = ?
                              WHERE currency = ? AND timeframe = ?;''', (json, currency, timeframe))
            if log == True:
                print('updated successfully   '+datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
        self.connection.commit()
        cursor.close()

    def getData(self, currency, timeframe, log=True):
        cursor = self.connection.cursor()
        cursor.execute('''SELECT json FROM data2 WHERE (currency=?) AND (timeframe=?);''', [currency, timeframe])
        records = cursor.fetchone()
        if log == True:
            print("data recieved   "+datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
        self.connection.commit()
        cursor.close()
        records=records[0]
        records=json.loads(records)
        records = [x[0:] for x in records]
        records = [[x[0], float(x[1]), float(x[2]), float(x[3]), float(x[4]), float(x[5])] for x in records]
        return records