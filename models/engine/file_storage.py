#!/usr/bin/env python3
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
"""
a module that defines a file storage class
"""


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns:
            the dictionary __objects
        """

        return(self.__objects)

    def new(self, obj):
        """
         sets in __objects the obj with key <obj class name>.id
        """

        self.__objects[obj.__class__.__name__ + '.' + str(obj.id)] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        """
        with open(self.__file_path, "w+") as f:
            dict_tmp = {}
            for key, obj in self.__objects.items():
                dict_tmp[key] = obj.to_dict()
            json.dump(dict_tmp, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        only if the JSON file(__file_path) exists
        otherwise, do nothing. if the file doesn't exist, no
        exception should be raised
        """

        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                datas = json.load(f)
                for val in datas.values():
                    className = val["__class__"]
                    self.new(eval(className)(**val))
