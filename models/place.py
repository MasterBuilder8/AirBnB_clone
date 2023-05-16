#!/usr/bin/python3
"""
Module that defines a place  class that
inherits from BaseModel
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    class place that holds details of place
    """
    city_id = ""
    user_id = ""
    description = ""
    name = ""
    number_bathrooms = 0
    number_rooms = 0
    max_guest = 0
    price_by_night = 0
    longitude = 0.0
    latitude = 0.0
    amenity_ids = ""
