import os
import sys

from flask import Flask
from flask import jsonify
from flask import request

from exceptions import HTTPError

from dataloader import dfs, parse_polygon


FLASK_DEBUG = os.environ.get('FLASK_DEBUG', False)
app = Flask(__name__)

@app.route("/ping")
def ping():
    return "pong"

@app.route("/risqs")
def get_location_risqs():
    lat = request.args.get('lat')
    lon = request.args.get('long')
    print('long {} , lat : {}'.format(lon, lat), file=sys.stderr)
    ret = dfs.iloc[[0, 1]]
    ret['GEOMETRIE'] = ret['GEOMETRIE'].apply(lambda x: parse_polygon(x))
    return ret.to_json(orient='records')

@app.errorhandler(HTTPError)
def handle_http_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


if __name__ == "__main__":
    app.run(debug=FLASK_DEBUG, host='0.0.0.0', port=5005)