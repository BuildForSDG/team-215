import json
import traceback
from flask import request, jsonify, Blueprint

from app.utils.decorators import ApiRequest
from app.user.services import UserService

user = Blueprint('user', __name__)
api_request = ApiRequest()


# /api/v1/user/record
@user.route('/user/record', methods=["POST"])
@api_request.json  # check content-type = application.json in the request header
@api_request.required_body_params('user_id', 'record_data')  # validate request body
def user_record():
    request_data = json.loads(request.data.decode('utf-8'))
    record_data = request_data['record_data']

    if not isinstance(record_data, list):
        return jsonify(code="02", msg="Invalid data type,variable[record_data] must be of list type")

    result = UserService.add_user_record(request_data)
    if result is None:
        response = {"code": "02", "msg": "User doesnt exist"}
    else:
        response = {"code": "00", "msg": "User data recoded successfully"}

    return jsonify(response)

# /api/v1/user/record/1
@user.route('/user/record/<id>', methods=["GET"])
def get_user_record(id):

    result = UserService.get_user_record(id)
    if result is None:
        response = {"code": "02", "msg": "User record not found", "data": {}}
    else:
        response = {"code": "00", "msg": "User record retrieved successfully", "data": result}

    return jsonify(response)

