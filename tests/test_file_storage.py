#!/usr/bin/python3
import models
import unittest
from models.base_model import BaseModel
from models import storage
import os


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """
        Set up test environment
        """
        self.model = BaseModel()
        storage.save()
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
        storage.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_reload(self):
        """
        Test reload method of FileStorage
        """
        storage.save()
        storage._FileStorage__objects.clear()
        storage.reload()
        self.assertIn(f"BaseModel.{self.model.id}", storage.all())


if __name__ == '__main__':
    unittest.main()
