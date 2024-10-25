#!/usr/bin/env python3

import re
from app.models.base_model import BaseModel


class User(BaseModel):
    def __init__(self, first_name, last_name, email):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = False  # Default value

        # Validate attributes
        self.validate_attributes()

    def validate_attributes(self):
        if len(self.first_name) > 50 or len(self.last_name) > 50:
            raise ValueError("First and last name less than 50 characters.")

        if not self.validate_email(self.email):
            raise ValueError("Invalid email format.")

    @staticmethod
    def validate_email(email):
        """Basic email format validation."""
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(regex, email) is not None
