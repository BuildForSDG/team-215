from flask import Flask, jsonify
from flask_mongoengine import MongoEngine
from app.config import config

app = Flask(__name__)

app.config['MONGODB_DB'] = config.MONGODB_DB
app.config['MONGODB_HOST'] = config.MONGODB_HOST
app.config['MONGODB_PORT'] = config.MONGODB_PORT
app.config['MONGODB_USERNAME'] = config.MONGODB_USERNAME
app.config['MONGODB_PASSWORD'] = config.MONGODB_PASSWORD

db = MongoEngine(app)

from app.auth.controller import auth

app.register_blueprint(auth, url_prefix='/api/v1')


@app.errorhandler(404)
def not_found(error):
    return jsonify(code="404", msg="Resource not found"), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify(code="405", msg="Method not allowed"), 405
