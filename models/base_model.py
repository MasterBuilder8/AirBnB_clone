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
