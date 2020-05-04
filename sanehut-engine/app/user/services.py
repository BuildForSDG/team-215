
class UserService:
    """Class for User functionality"""

    @staticmethod
    def get_all_users():
        response = {
            "msg": "Welcome to the User Endpoint.",
            "data": {}
        }
        return response