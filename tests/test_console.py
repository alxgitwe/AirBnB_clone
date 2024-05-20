#!/usr/bin/python3

"""Defines custom tests for console.py."""
import os
import pep8
import unittest
import models
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

class CustomHBNBCommand(unittest.TestCase):
    """Custom tests for the HBNB command interpreter."""

    @classmethod
    def setUpClass(cls):
        """Setup for HBNBCommand testing."""
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass
        cls.custom_HBNB = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """Teardown for HBNBCommand testing."""
        try:
            os.rename("temp", "file.json")
        except IOError:
            pass
        del cls.custom_HBNB
        if type(models.storage) == DBStorage:
            models.storage._DBStorage__session.close()

    def setUp(self):
        """Reset FileStorage objects dictionary."""
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Delete any created file.json."""
        try:
            os.remove("file.json")
        except IOError:
            pass

    # Add your custom test methods here

if __name__ == "__main__":
    unittest.main()
