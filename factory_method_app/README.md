# Factory Method Flask Application

This project illustrates the Factory Method pattern for setting up a Flask application. It provides a structured and reusable way to initialize and configure the application, making it suitable for more complex projects.

## Overview
- **Purpose**: To demonstrate how to set up a Flask application using the Factory Method.
- **Features**:
  - Modular application setup.
  - Reusable `create_app` function for configuration and initialization.
  - Clean separation of concerns.

## Directory Structure
```
factory_app/
    app.py       # Entry point for running the application
    __init__.py  # Contains the `create_app` function
```

## Prerequisites
- Python (3.8 or later recommended)
- pip (Python package manager)

## Setup Instructions
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/Flask_beginer_to_advance.git
    cd Flask_beginer_to_advance/factory_app
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
    python app.py
    ```
    By default, the app will be accessible at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Code Highlights
### `__init__.py`
```python
from flask import Flask

def create_app():
    """
    Factory method for creating a Flask application.

    Returns:
        Flask app instance.
    """
    app = Flask(__name__)

    @app.route('/')
    def home():
        return "Hello MR./MISS., Welcome to the Factory Method App"

    return app
```
- **Factory Method**: `create_app` initializes and configures the application.
- **Route Definition**: Routes are defined within the factory function for modularity.

### app.py
```python
from factory_app import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
```
- **Entry Point**: `app.py` imports and runs the application created by `create_app`.

## Expected Output
When you visit [http://127.0.0.1:5000](http://127.0.0.1:5000), you should see:
```
Hello MR./MISS., Welcome to the Factory Method App
```

## Key Learning Points
- Understand the benefits of the Factory Method pattern for Flask applications.
- Learn how to separate app initialization from runtime configuration.
- Create reusable and testable app initialization code.

## Next Steps
Explore the `blueprint_app` project to understand how to further modularize Flask applications using blueprints.

