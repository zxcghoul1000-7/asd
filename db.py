import sqlite3


class sqliteDb:
    def __init__(self):
        self.connection = sqlite3.connect('source_data.db')
        print("connected to db")

    def close(self):
        self.connection.close()
        print("db is closed")

    def addToDb(self, open_time, open_value, high_value, low_value, close_value, currency, interval):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO data (openTime,openValue, highValue,lowValue,closeValue,currency,interval) 
                       VALUES (?,?,?,?,?,?,?);''', (open_time, open_value, high_value, low_value, close_value, currency, interval))
        print('recorded successfully')
        self.connection.commit()
        cursor.close()

    def clear(self):
        cursor = self.connection.cursor()
        cursor.executescript('''DELETE FROM COMPANY;
                             VACUUM;''')
        print('recorded successfully')
        self.connection.commit()
        cursor.close()
