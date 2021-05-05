import psycopg2
from psycopg2 import Error


class Db:
    def __init__(self):
        self.connection = psycopg2.connect(user="postgres",
                                           # пароль, который указали при установке PostgreSQL
                                           password="toor",
                                           host="127.0.0.1",
                                           port="5432",
                                           database="postgres_db")

    def close(self):
        self.connection.close()
        print("db is closed")

    def createTable(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS public.debili(         
                          "id" serial NOT NULL,
                          "name" text NOT NULL,
                          "rank" text NOT NULL,
                          PRIMARY KEY ("id")
                                                );''')
        print('table created successfully')
        self.connection.commit()
        cursor.close()

    def addToDb(self, name, rank):
        cursor = self.connection.cursor()
        cursor.execute(
            '''INSERT INTO debili (name,rank) VALUES (%s,%s);''', (name, rank))
        print('recorded successfully')
        self.connection.commit()
        cursor.close()

    def deleteByName(self, name):
        cursor = self.connection.cursor()
        cursor.execute('''DELETE FROM debili WHERE name = %s;''', [name])
        print('deleted successfully')
        self.connection.commit()
        cursor.close()

    def changeRankById(self, id, new_rank):
        cursor = self.connection.cursor()
        cursor.execute(
            '''UPDATE debili SET rank = %s WHERE id = %s;''', (new_rank, id))
        print('updated successfully')
        self.connection.commit()
        cursor.close()

    def deleteTable(self):
        cursor = self.connection.cursor()
        cursor.execute('''DROP TABLE IF EXISTS debili;''')
        print("table deleted")
        self.connection.commit()
        cursor.close()

    def getByRank(self, rank):
        cursor = self.connection.cursor()
        cursor.execute('''SELECT * FROM debili WHERE rank=%s;''', [rank])
        records = cursor.fetchall()
        print("spizheno successfully")
        self.connection.commit()
        cursor.close()
        return records
