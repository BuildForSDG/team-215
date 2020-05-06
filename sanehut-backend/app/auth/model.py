from app.application import db
import datetime


class Auth(db.Document):
    """Class for Auth Model"""
    firstName = db.StringField(required=True)
    lastName = db.StringField(required=True)
    email = db.StringField(required=True, unique=True)
    password = db.StringField(required=True, unique=True)
    phoneNumber = db.StringField(required=True)
    userType = db.StringField(required=True)
    created_at = db.DateTimeField(default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<Auth %r>' % self.id

    def to_dict(self, include_password=False):
        dict_obj = {}

        for column, value in self._fields.items():
            if column == "password":
                if include_password:
                    dict_obj[column] = getattr(self, column)
            else:
                dict_obj[column] = getattr(self, column)

        if "id" in dict_obj:
            dict_obj["id"] = str(dict_obj["id"])

        return dict_obj
