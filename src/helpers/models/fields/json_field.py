import json

from django.db import models


class JSONField(models.TextField):
    """JSONField is a generic textfield that neatly serializes/unserializes
    JSON objects seamlessly"""

    def to_python(self, value):
        """Convert our string value to JSON after we load it from the DB"""

        if value == "" or value is None:
            return None
        elif isinstance(value, str):
            value = json.loads(value)
        else:
            raise TypeError("Not valid value type in db")

        return value

    def from_db_value(self, value, expression, connection):
        return self.to_python(value)

    def get_prep_value(self, value):
        """Convert our JSON object to a string before we save"""

        if isinstance(value, (dict, list)):
            value = json.dumps(value)
        elif value == "" or value is None:
            pass
        else:
            raise TypeError(f"Not valid value type. ValueType={type(value)}")
        return value

    def value_from_object(self, obj):
        return json.dumps(super().value_from_object(obj))
