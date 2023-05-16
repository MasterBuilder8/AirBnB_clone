#!/usr/bin/python3
"""
Module that serializes instances to a JSON file and 
deserializes JSON file to instances.
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage():
    """
    A class that serializes instances to a JSON file and 
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        data = {}
        val = None
        for key, val in FileStorage.__objects.items():
            if hasattr(val.__class__, "to_dict"):
                data[key] = val.__class__.to_dict(val)
                break
            if val:
                data[key] = val.to_dict()

            with open(FileStorage.__file_path, "w") as file:
                json.dump(data, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r") as file:
                obj = {'BaseModel': BaseModel, 'User':User, 'Place':Place,
                        'State':State, 'City':City, 'Amenity':Amenity,
                        'Review':Review}
                data = json.load(file)

                for key, value in data.items():
                    obj[key] = eval(key.split('.')[0](**value)
                FileStorage.__objects = obj
            except FileNotFoundError:
             pass
