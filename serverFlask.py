from flask import Flask, request
import json
from test import Db
app = Flask(__name__)
database = Db()


@app.route("/get", methods=['GET'])
def get_all_extrems():
    rank = request.args.get('rank')
    ghouls = database.getByRank(rank)
    return json.dumps(ghouls)


@app.route("/post", methods=['POST'])
def get_all_extrems2():
    content = request.json
    database.addToDb(content['name'], content['rank'])
    return content


if __name__ == "__main__":
    app.run(port=8081)
