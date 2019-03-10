import os
import sys

from flask import Flask
from flask import jsonify
from flask import request
from flask import Response

from flask_cors import CORS
from flaskext.mysql import MySQL


from exceptions import HTTPError
from calculate_distance import compute_distances, compute_bornes_distances

from dataloader import dfs, dfs_bornes['COORDONNEES']

FLASK_DEBUG = os.environ.get('FLASK_DEBUG', False)
app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'risqc'
app.config['MYSQL_DATABASE_HOST'] = '0.0.0.0'
mysql.init_app(app)

CORS(app)

@app.route("/ping")
def ping():
    return "pong"

@app.route("/risqs")
def get_location_risqs():
    lat = request.args.get('lat')
    lon = request.args.get('long')
    point_coord = [lon, lat]
    print('long {} , lat : {}'.format(lon, lat), file=sys.stderr)
    top_min = compute_distances(point_coord, dfs)
    #A PLUGGER
    bornes = compute_bornes_distances(point_coord, dfs_bornes)

    return Response(top_min.to_json(orient='recor   ds'), mimetype='application/json')
    
@app.errorhandler(HTTPError)
def handle_http_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


if __name__ == "__main__":
    app.run(debug=FLASK_DEBUG, host='0.0.0.0', port=5005)