from app.auth.model import Auth


class AuthService:
    """Class for User functionality"""

    @staticmethod
    def find_by_email(email: str):
        try:
            user_data = Auth.objects(email=email).first()
            if user_data is not None:
                user_data = user_data.to_dict()
        except Exception as ex:
            user_data = None
            print("Exception Occurred | {0}".format(str(ex)))
        return user_data

    @staticmethod
    def find_by_id(user_id: str):
        try:
            user_data = Auth.objects(id=user_id).first()
            if user_data is not None:
                user_data = user_data.to_dict()
        except Exception as ex:
            user_data = None
            print("Exception Occurred | {0}".format(str(ex)))
        return user_data

    def find_email_password(email: str, include_password=True):
        try:
            user_data = Auth.objects(email=email).first()
            if user_data is not None:
                user_data = user_data.to_dict(include_password=include_password)
        except Exception as ex:
            user_data = None
            print("Exception Occurred | {0}".format(str(ex)))
        return user_data

    @staticmethod
    def add_user(data):
        try:
            add_user = Auth()
            add_user.firstName = data['firstName'].strip()
            add_user.lastName = data['lastName'].strip()
            add_user.email = data['email'].strip()
            add_user.password = data['password_hash'].strip()
            add_user.phoneNumber = data['phoneNumber'].strip()
            add_user.userType = data['userType'].strip()

            add_user.save()
            add_user = add_user.to_dict()
        except KeyError as kex:
            print("Exception Occurred | {0}".format(str(kex)))
            raise kex
        except Exception as ex:
            print("Exception Occurred | {0}".format(str(ex)))
            raise ex
        return add_user

    @staticmethod
    def update_user(data):
        try:
            user_data = Auth.objects(email=data["email"]).first()
            if user_data is None:
                user_data = None
                return user_data
            if "firstName" in data:
                user_data.firstName = data["firstName"].strip()
            if "lastName" in data:
                user_data.lastName = data["lastName"].strip()
            if "email" in data:
                user_data.email = data["email"].strip()
            if "password" in data:
                user_data.password = data["password"].strip()
            if "phoneNumber" in data:
                user_data.phoneNumber = data["phoneNumber"].strip()
            if "userType" in data:
                user_data.userType = data["userType"].strip()

            user_data.save()
            user_data = user_data.to_dict()
        except KeyError as kex:
            print("Exception Occurred | {0}".format(str(kex)))
            raise kex
        except Exception as ex:
            print("Exception Occurred | {0}".format(str(ex)))
            raise ex
        return user_data

