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
