from flask import Flask
from .home.routes import home_bp  # Import the home blueprint from the home module

def create_app():
    app = Flask(__name__)

    # Register the Blueprint with a URL prefix '/home'
    app.register_blueprint(home_bp, url_prefix='/home')

    return app
