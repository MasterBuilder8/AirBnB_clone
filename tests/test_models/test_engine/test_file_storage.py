#!/usr/bin/python3
"""
Test module for storage
"""


from datetime import datetime
import unittest
import json
from time import sleep
from models.engine.file_storage import FileStorage


class test_filestorage(unittest.Testcase):
    """Test FileStorage class"""
    def test_instances(self):
        """instantiation"""
        obj = FileStorage
        self.assertIsInstance(obj, FileStorage)


    def test_docs(self):
        """Test docstring"""
        self.assertIsNotNone(FileStorage.all)
        self.assertIsNotNone(FileStorage.new)
        self.assertIsNotNone(FileStorage.save)
        self.assertIsNotNone(FileStorage.reload)

        if __name__ == '__main__':
            unittest.main()
