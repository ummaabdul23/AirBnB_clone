#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:

    def __init__(self):
        # Generate a unique ID for each instance
        self.id = str(uuid.uuid4())
        # Set the created_at attribute to the current date and time
        self.created_at = datetime.now()
        # Set the updated_at attribute to the current date and time
        self.updated_at = datetime.now()

    def __str__(self):
        # Return a string representation of the instance
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        # Update the updated_at attribute to the current date and time
        self.updated_at = datetime.now()

    def to_dict(self):
        # Create a dictionary copy of the instance's attributes
        dict_representation = self.__dict__.copy()
        # Add the __class__ key with the name of the class
        dict_representation["__class__"] = self.__class__.__name__
        # Convert created_at and updated_at to ISO format strings
        dict_representation["created_at"] = self.created_at.isoformat()
        dict_representation["updated_at"] = self.updated_at.isoformat()
        return dict_representation
