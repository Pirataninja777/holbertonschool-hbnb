# HBnB API

A scalable API structure for the HBnB application, with a modular design.

## Project Structure
- **app/**: Core application
  - **api/**: API endpoints, organized by version
  - **models/**: Business logic classes
  - **services/**: Facade pattern for layer communication
  - **persistence/**: In-memory repository (planned for database integration)
- **run.py**: Entry point for the application
- **config.py**: Application configuration
- **requirements.txt**: Project dependencies

## Setup
1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Run the application:
    ```bash
    python run.py
    ```

## Dependencies
- Flask
- Flask-RESTxi

## Business Logic Layer

The Business Logic Layer (BLL) includes classes for managing entities in the HBnB application. Each class handles specific business operations and entity relationships.

### Classes

1. **User**: Represents a user with attributes like `first_name`, `last_name`, `email`, and `is_admin`.
2. **Place**: Represents a place with attributes like `title`, `price`, `latitude`, `longitude`, and an `owner` (User instance).
3. **Review**: Links a user and a place, with attributes `text` (review content) and `rating` (1-5).
4. **Amenity**: Represents an amenity (e.g., "Wi-Fi").

### Usage Example

```python
# Create a User
user = User(first_name="John", last_name="Doe", email="john@example.com")

# Create a Place owned by the User
place = Place(title="Beach House", price=150.0, latitude=34.0522, longitude=-118.2437, owner=user)

# Add an Amenity to the Place
amenity = Amenity(name="Pool")
place.add_amenity(amenity)

# Add a Review to the Place
review = Review(text="Great place to stay!", rating=5, place=place, user=user)
place.add_review(review)
