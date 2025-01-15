from flask import Flask 

def create_app():
    app = Flask(__name__)
    
    from blueprint_app.home.routes import bp_route
    app.register_blueprint(bp_route)
    return app

