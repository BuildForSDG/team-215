import json
import traceback
from flask import request, jsonify, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash

from app.auth.services import AuthService
from app.utils.decorators import ApiRequest
from app.utils.helper import Helper

auth = Blueprint('auth', __name__)
api_request = ApiRequest()


# /api/v1/login
@auth.route('/login', methods=["POST"])
@api_request.json  # check content-type = application.json in the request header
@api_request.required_body_params('email', 'password')  # validate request body
def login():
    request_data = json.loads(request.data.decode('utf-8'))
    email = request_data['email']
    password = request_data['password']

    existing_user = AuthService.find_email_password(email)

    if existing_user is None:
        return jsonify(code="02", msg="Invalid email and/or password")

    check_password = check_password_hash(existing_user['password'], password)
    if not check_password:
        return jsonify(code="02", msg="Invalid email and/or password")
    del existing_user['password']
    return jsonify(code="00", msg="User login successfully", data=existing_user)


# /api/v1/signup
@auth.route('/signup', methods=["POST"])
@api_request.json  # check content-type = application.json in the request header
@api_request.required_body_params('firstName', 'lastName', 'email', 'password', 'phoneNumber',
                                  'userType')  # validate request body
def signup():
    request_data = json.loads(request.data.decode('utf-8'))
    email = request_data['email']
    password = request_data['password']

    if not Helper.is_valid_email(email):
        return jsonify(code="02", msg="Invalid email address")
    existing_user = AuthService.find_by_email(email)
    if existing_user is not None:
        return jsonify(code="02", msg="User already exist")

    password_hash = generate_password_hash(password)
    request_data['password_hash'] = password_hash
    try:
        new_user_data = AuthService.add_user(request_data)
    except Exception as ex:
        traceback.format_exc()
        print("Exception Occurred | {0}".format(str(ex)))

    return jsonify(code="00", msg="User signed up successfully", data=new_user_data)


# /api/v1/forgot
@auth.route('/forgot', methods=["POST"])
@api_request.json  # check content-type = application.json in the request header
@api_request.required_body_params('email', 'newPassword')  # validate request body
def forgot():
    request_data = json.loads(request.data.decode('utf-8'))
    email = request_data['email']
    newPassword = request_data['newPassword']

    if not Helper.is_valid_email(email):
        return jsonify(code="02", msg="Invalid email address")

    new_password_hash = generate_password_hash(newPassword)
    request_data['password'] = new_password_hash
    try:
        new_user_data = AuthService.update_user(request_data)
        if new_user_data is None:
            return jsonify(code="02", msg="User doesnt exist")
    except Exception as ex:
        traceback.format_exc()
        print("Exception Occurred | {0}".format(str(ex)))

    return jsonify(code="00", msg="User password changed successfully")
