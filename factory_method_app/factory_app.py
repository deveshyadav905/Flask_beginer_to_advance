from flask import Flask

"""Factory Method for Flask App
This app demonstrates the use of the Factory Method pattern to create a Flask app.
- The `create_app()` function is used to create and configure the Flask app.
- It allows for flexibility in the app's structure and is useful when adding features like Blueprints or different configurations.

Usage:
1. The `create_app()` function will be called to create a Flask instance.
2. The app will respond to the root URL ('/') with a simple greeting message.

This structure is great for more advanced applications where you might want to separate different components of your app.

In this app, a simple greeting message is returned when accessing the root route.
"""
def create_app():
    app = Flask(__name__)
    
    @app.route('/')
    def home_route():
        return "Hello MR./MISS., Welcome to the Factory Method App"    
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
