from app.application import db
import datetime


class User(db.Document):
    """Class for User Model"""
    user_id = db.StringField(required=True)
    record_data = db.ListField(required=True)
    updated_at = db.DateTimeField(null=True, default=None)

    def __repr__(self):
        return '<User %r>' % self.id

    def to_dict(self):
        dict_obj = {}

        for column, value in self._fields.items():
            dict_obj[column] = getattr(self, column)

        if "id" in dict_obj:
            dict_obj["id"] = str(dict_obj["id"])

        return dict_obj
