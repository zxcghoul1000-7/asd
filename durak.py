from test import Db
database = Db()
for i in database.getByRank('pivo'):
    print(i)
