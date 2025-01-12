#!/usr/bin/python3
"""setup API"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import environ

from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_app(session):
    """remove sqlalchemy session"""
    storage.close()


@app.errorhandler(404)
def not_found_error(error):
    """ 404 error"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
