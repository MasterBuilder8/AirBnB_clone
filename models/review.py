#!/usr/bin/python3
"""
a class Review that inherits from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    class that holds the review attribute
    """
    text = ""
    user_id = ""
    place_id = ""
