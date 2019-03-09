import os
import sys

from flask import Flask
from flask import jsonify
from flask import request

from exceptions import HTTPError


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
    return jsonify([])

@app.errorhandler(HTTPError)
def handle_http_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


if __name__ == "__main__":
    app.run(debug=FLASK_DEBUG, host='0.0.0.0', port=5005)