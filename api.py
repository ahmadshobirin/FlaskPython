import flask
from flask import request, jsonify


app = flask.Flask(__name__)
app.config["DEBUG"] = True

datas = [
    {
        'id' : 1,
        'title': "Awewe",
    },
    {
        'id' : 2,
        'title': "Uwuwu",
    }

]


@app.route('/', methods=['GET'])
def home():
    return "<h1>Jasik Kenek wkwkwk</h1><p>Flask Pyton API.</p>"

@app.route('/authors', methods=['GET'])
def authors():
    return "Ahmad Shobirin"

@app.route('/datas', methods=["GET"])
def all():
    return jsonify(datas);

@app.route('/data', methods=["GET"])
def getId():

    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No Id field provided."

    results = []

    for data in datas:
        if data['id'] == id:
            results.append(data)

    return jsonify(results)
app.run()