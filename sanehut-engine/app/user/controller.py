import json
from flask import request, jsonify, Blueprint
from app.user.services import UserService
 
user = Blueprint('user', __name__)
 
# /api/v1/users
@user.route('/users', methods = ["GET"])
def home():
    result = UserService.get_all_users()
    return jsonify(result), 200