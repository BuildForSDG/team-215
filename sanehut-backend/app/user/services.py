
from app.user.model import User
from app.auth.services import AuthService
import datetime


class UserService:

    @staticmethod
    def add_user_record(data):
        try:
            user_data = AuthService.find_by_id(data['user_id'])
            if user_data is None:
                response = None
                return response
            user_data_record = User.objects(user_id=data['user_id']).first()

            if user_data_record is None:
                add_user_record = User()
                add_user_record.user_id = data['user_id'].strip()
                add_user_record.record_data = data['record_data']
                add_user_record.updated_at = datetime.datetime.utcnow

                add_user_record.save()
                response = add_user_record.to_dict()
                return response

            user_data_record.record_data = data['record_data']
            user_data_record.updated_at = datetime.datetime.utcnow
            user_data_record.save()

        except KeyError as kex:
            print("Exception Occurred | {0}".format(str(kex)))
            raise kex
        except Exception as ex:
            print("Exception Occurred | {0}".format(str(ex)))
            raise ex
        return user_data_record

    @staticmethod
    def get_user_record(user_id):
        try:
            user_data = User.objects(user_id=user_id).first()
            if user_data is not None:
                user_data = user_data.to_dict()
        except Exception as ex:
            user_data = None
            print("Exception Occurred | {0}".format(str(ex)))
            raise ex
        return user_data
