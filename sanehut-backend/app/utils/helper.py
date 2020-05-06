import re


class Helper:
    @staticmethod
    def is_valid_email(email):
        import re
        return re.search('^[A-Za-z0-9+_.\-]+@(.+)\.(.+)$', email) is not None
