# Blueprint Flask Application

This project demonstrates how to structure a Flask application using Blueprints. Blueprints allow for modularization, enabling a cleaner and more maintainable codebase, especially for larger applications.

## Overview
- **Purpose**: To organize the application into smaller, reusable components.
- **Features**:
  - Define Blueprints to separate application logic.
  - Register Blueprints within the main application.
  - Serve routes defined in the Blueprint module.

## Directory Structure
```
blueprint_app/
    __init__.py        # Initializes the main application with Blueprints
    home/
        __init__.py    # Initializes the Blueprint for the 'home' module
        routes.py      # Contains routes for the 'home' Blueprint
```

## Prerequisites
- Python (3.8 or later recommended)
- pip (Python package manager)

## Setup Instructions
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/Flask_beginer_to_advance.git
    cd Flask_beginer_to_advance/blueprint_app
    ```

2. **Set Up a Virtual Environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Flask**:
    ```bash
    pip install flask
    ```

4. **Run the Application**:
    ```bash
    flask run
    ```
    By default, the app will be accessible at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Code Highlights
### __init__.py (Main Application)
```python
from flask import Flask
from .home.routes import home_bp  # Import the Blueprint

def create_app():
    app = Flask(__name__)

    # Register the Blueprint
    app.register_blueprint(home_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
```
- **Blueprint Registration**: `app.register_blueprint(home_bp)` adds the routes from the `home` module to the main application.

### home/__init__.py
```python
from flask import Blueprint

# Initialize the Blueprint
home_bp = Blueprint('home', __name__)
```

### home/routes.py
```python
from . import home_bp

@home_bp.route('/')
def home():
    return "Hello from the Home Blueprint!"
```
- **Route Definition**: `@home_bp.route('/')` defines a route for the `home` Blueprint.

## Expected Output
When you visit [http://127.0.0.1:5000](http://127.0.0.1:5000), you should see:
```
Hello from the Home Blueprint!
```

## Key Learning Points
- Modularize Flask applications using Blueprints.
- Understand how to define and register Blueprints.
- Separate concerns by grouping related routes into specific modules.

## Next Steps
Explore more advanced Blueprint use cases, such as handling templates and static files, or move to the `template_app` project for integrating HTML templates with Flask.

