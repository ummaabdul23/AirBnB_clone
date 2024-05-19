#!/usr/bin/python3
import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):

    def setUp(self):

        """
        Set up test environment
        """
        self.model = BaseModel()
        self.storage.new(self.model)
        self.file_path = storage._FileStorage__file_path

    def tearDown(self):

        """
        Clean up test environment
        """
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        storage._FileStorage__objects.clear()

    def test_save(self):
        """
        Test save method of FileStorage
        """
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_reload(self):
        """
        Test reload method of FileStorage
        """
        self.storage.save()
        self.storage._FileStorage__objects.clear()
        self.storage.reload()
        self.assertIn(f"BaseModel.{self.model.id}", self.storage.all())

    def test_all(self):
            """
            Test the all method returns the correct objects.
            """
            self.assertEqual(dict, type(self.storage.all()))


    def test_new(self):
           """
           Test the new method sets the correct object.
           """
           self.assertIn(f"BaseModel.{self.model.id}", self.storage.all())


if __name__ == '__main__':
    unittest.main()
