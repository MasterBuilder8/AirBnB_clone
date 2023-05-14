#!/usr/bin/python3
"""The 'BaseModel' module defines a base class 'BaseModel' that 
provides common attributes and methods that can be used by other classes in the application."""


import uuid
from datetime import datetime
from models import  storage


class BaseModel:
    """Base Model Class

    This is the Base Model that take care of the
    initialization, serialization and deserialization
    of the future instances"""
    def __init__(self, *args, **kwargs):
        """initializes the base  instance

        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "update_at":
                    self.__dict__["update_at"] = datetime.strptime(
                            kwargs["update_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self__dict__[key] = kwargs[key]
                else:
                    self.id = str(uuid.uuid4())
                    self.created_at = datetime.now()
                    self.updated_at = datetime.now()
                    storage.new(self)

        def __str__(self):
            """returns  string representation of an instance
            in a readable format"""

            return "[{}] ({}) {}".\
                    format(type(self).__name__, self.id, self.__dict__)

        def save(self):
            """Updates the 'update_at' with the  current date and time"""

            self.update_at = datetime.now()
            storage.save()

        def to_dict(self):
            """returns a dictionary representation of an instance""""

            my_dict = self.

        

