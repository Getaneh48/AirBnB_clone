#!/usr/bin/python3
"""
a module that define a a class BaseModel for all common
attributes/methods for other classes
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    A class that defines all common attributes/methods
    for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        initializes the class

        Args:
            args: list of arguments (list)
            kwargs: keyworded arguments (dictionary)
        """
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key in ["updated_at", "created_at"]:
                    dts = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    self.__dict__[key] = dts
                elif key == '__class__':
                    pass
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """
        Updates the public instance attribute updated_at with the current
        datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of
        the instance
        """
        mydict = self.__dict__.copy()
        mydict['__class__'] = self.__class__.__name__
        mydict['created_at'] = self.created_at.isoformat()
        mydict['updated_at'] = self.updated_at.isoformat()

        return mydict

    def __str__(self):
        """
        Returns:
        string represntation of the current object
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
