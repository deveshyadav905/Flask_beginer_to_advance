# Flask App with Configuration

This project demonstrates how to use configuration classes to manage environment-specific settings in a Flask application. It introduces a more structured approach compared to a single-file application.

## Overview
- **Purpose**: To showcase how to use configuration files in Flask.
- **Features**:
  - Centralized configuration management.
  - Environment-specific settings (e.g., Development, Production).
  - Clean separation of concerns between application logic and settings.

## Directory Structure
```
config_app/
    app.py         # Entry point for the Flask application
    config.py      # Contains configuration classes for different environments
```

## Prerequisites
- Python (3.8 or later recommended)
- pip (Python package manager)

## Setup Instructions
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/Flask_beginer_to_advance.git
    cd Flask_beginer_to_advance/config_app
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
### app.py
```python
from flask import Flask
from config import DevelopmentConfig, ProductionConfig

# Application Factory Function
def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)

    # Load configuration from the specified class
    app.config.from_object(config_class)

    @app.route('/')
    def hello():
        return f"Hello, this is a {app.config['ENV']} environment!"

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
```

### config.py
```python
class Config:
    """Base configuration class with common settings."""
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'supersecretkey'

class DevelopmentConfig(Config):
    """Configuration for the development environment."""
    DEBUG = True
    ENV = 'development'

class ProductionConfig(Config):
    """Configuration for the production environment."""
    DEBUG = False
    ENV = 'production'
```

## Key Learning Points
- **Configuration Classes**: Use Python classes to define settings for different environments.
- **Environment-Specific Settings**: Switch between configurations easily (e.g., Development vs. Production).
- **Clean Code**: Centralize configuration logic for better maintainability.

## Expected Output
- When running the app with `DevelopmentConfig`, visiting [http://127.0.0.1:5000](http://127.0.0.1:5000) will display:
  ```
  Hello, this is a development environment!
  ```
- When running the app with `ProductionConfig`, the message will change to:
  ```
  Hello, this is a production environment!
  ```

## Next Steps
Proceed to the **factory_app** project to explore modular app creation with Flask's factory method.

