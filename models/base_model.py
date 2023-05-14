#!/usr/bin/env python3
"""This is a file that defines our basemodel
class that will be used throughout the project"""

import uuid
import models
from datetime import datetime


class BaseModel:
    """This is a class that defines all
    common methods/attibutes for other classes"""

    def __init__(self, *args, **kwargs):
        """initializing id, created_at and
        updated_at public instance attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    dt_format = "%Y-%m-%dT%H:%M:%S.%f"
                    self.__dict__[key] = datetime.strptime(value, dt_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """string that returns
        '[<class name>] (<self.id>) <self.__dict__>'"""
        class_name = self.__class__.__name__
        obj_id = self.id
        obj_dict = self.__dict__
        return "[{}] ({}) {}".format(class_name, obj_id, obj_dict)

    def save(self):
        """This function updates the public instance attribute
        updated_at wirh the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """a function that returns a dictionary
        containing all keys/values of __dict__ of the instance"""
        dictionary = dict(self.__dict__)
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
