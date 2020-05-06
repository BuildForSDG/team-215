from functools import wraps
import json
import traceback
from flask import g
from flask import jsonify
from flask import request


class ApiRequest:

    def json(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            request_headers = dict(request.headers)
            if 'Content-Type' not in request_headers or 'application/json' not in request_headers['Content-Type']:
                return jsonify(code="02", msg="JSON is required for this API - Kindly set the Content-Type to "
                                              "application/json")
            elif request.data is None:
                return jsonify(code="02", msg="JSON data required"), 200
            try:
                json_data = json.loads(request.data.decode('utf-8'))
            except Exception as ex:
                traceback.print_exc()
                print("Exception Occurred | {0}".format(str(ex)))
                return jsonify(code="02", msg="Invalid JSON Data format"), 200

            return func(*args, **kwargs)

        return wrapper

    def required_body_params(self, *required_params):
        def wrapper(f):
            @wraps(f)
            def wrapped(*args, **kwargs):
                try:
                    request_data = json.loads(request.data.decode('utf-8'))
                except Exception as ex:
                    traceback.print_exc()
                    print("Exception Occurred | {0}".format(str(ex)))
                    return jsonify(code="02", msg="Invalid JSON Data format"), 200

                missing_params = []
                for param in required_params:
                    if param not in request_data or str(request_data[param]) == "":
                        missing_params.append(param)

                if len(missing_params) > 0:
                    response = {
                        "code": "02",
                        "msg": "Missing and/or blank parameters: {}".format(', '.join(missing_params))
                    }
                    return jsonify(**response), 200
                return f(*args, **kwargs)

            return wrapped

        return wrapper
