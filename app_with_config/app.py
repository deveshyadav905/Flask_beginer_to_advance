from flask import Flask
from config import DevelopmentConfig, ProductionConfig  # Import your config classes

"""Flask App with Configurations (Development and Production)
This app demonstrates how to use different configurations based on the environment.
- We use a `Config` class as a base, with separate configurations for Development and Production.
- The `DevelopmentConfig` includes debugging options, while `ProductionConfig` disables debugging and includes production settings.

To run:
1. In a development environment, use the `DevelopmentConfig` to enable debugging.
2. In production, use the `ProductionConfig` to disable debugging and secure settings.

This structure helps to manage configurations for different environments in a clean way.

Usage:
- To use the app, make sure to import the correct configuration class based on the environment.
"""
def create_app(config_class=DevelopmentConfig):  # Default to DevelopmentConfig
    app = Flask(__name__)
    
    # Load configuration based on the passed class
    app.config.from_object(config_class)

    @app.route('/')
    def hello():
        return f"Hello, this is a {app.config['ENV']} environment!"
    
    return app
