#!/usr/bin/python3
"""Module that initializes storage variable"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
