from flask import Blueprint

bp_route = Blueprint("home",__name__)

@bp_route.route('/',methods=['GET'])
def say_hello():
    
    return "Welcome to the flask blueprint implementation"

