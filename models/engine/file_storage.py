#!/usr/bin/bash python3
"""A file containing class FileStorage that serializes instances
 to a JSON file and deserializes JSON file to instances"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """a class that serializes instances to a JSON
    file and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns a dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """method that sets in __objects the obj with key
        <obj class name>.id"""
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path"""
        with open(FileStorage.__file_path, "w", encoding='utf-8') as file:
            dict_storage = {}
            for key, val in FileStorage.__objects.items():
                dict_storage[key] = val.to_dict()
            json.dump(dict_storage, file)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists"""
        try:
            with open(FileStorage.__file_path, encoding='utf-8') as f:
                objects = json.load(f)
                for object in objects.values():
                    name = object['__class__']
                    del object['__class__']
                    self.new(eval(name)(**object))
        except FileNotFoundError:
            return
