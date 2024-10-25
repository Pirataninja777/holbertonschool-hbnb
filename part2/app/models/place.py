#!/usr/bin/env python3

from app.models.base_model import BaseModel


class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner  # User instance
        self.reviews = []  # List to store related reviews
        self.amenities = []  # List to store related amenities

        # Validate attributes
        self.validate_attributes()

    def validate_attributes(self):
        if len(self.title) > 100:
            raise ValueError("Title must be less than 100 characters.")

        if self.price <= 0:
            raise ValueError("Price must be a positive value.")

        if not (-90.0 <= self.latitude <= 90.0):
            raise ValueError("Latitude must be between -90.0 and 90.0.")

        if not (-180.0 <= self.longitude <= 180.0):
            raise ValueError("Longitude must be between -180.0 and 180.0.")

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)
