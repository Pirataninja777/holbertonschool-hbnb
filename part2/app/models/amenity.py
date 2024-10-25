#!/usr/bin/env python3

from app.models.base_model import BaseModel


class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = name

        # Validate attributes
        self.validate_attributes()

    def validate_attributes(self):
        if len(self.name) > 50:
            raise ValueError("name 50 characters max.")
