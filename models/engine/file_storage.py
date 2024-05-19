#!/usr/bin/python3
import datetime
import json
import os


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as file:
            json_objects = {key: obj.to_dict() for key,
                            obj in self.__objects.items()}
            json.dump(json_objects, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists)
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                json_objects = json.load(file)
                for key, obj_dict in json_objects.items():
                    class_name = key.split('.')[0]
                    self.__objects[key] = eval(class_name)(**obj_dict)
