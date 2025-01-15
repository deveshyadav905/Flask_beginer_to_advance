from flask import Blueprint

# Create the Blueprint for 'home'
home_bp = Blueprint('home', __name__)

@home_bp.route('/profile')
def profile():
    return "This is the user profile page."

@home_bp.route('/login')
def login():
    return "This is the login page."

@home_bp.route('/logout')
def logout():
    return "This is the logout page."
