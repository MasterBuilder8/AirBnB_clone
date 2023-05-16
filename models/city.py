#!/usr/bin/python3
"""Module that defines a class city"""
from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    """this is class city"""
    state_id = ""
    name = ""
