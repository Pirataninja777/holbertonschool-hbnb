#!/usr/bin/env python3

import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())  # Generate a unique identifier
        self.created_at = datetime.now()  # Set creation timestamp
        self.updated_at = datetime.now()  # Set update timestamp

    def save(self):
        """Update the updated_at timestamp."""
        self.updated_at = datetime.now()

    def update(self, data):
        """Update the attributes based on a provided dictionary."""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()  # Call save to update updated_at
