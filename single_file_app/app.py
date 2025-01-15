from flask import Flask

"""Starting with Single File Application
This is a simple Flask app that starts a server and shows a greeting message.
- The app listens on localhost at '127.0.0.1:5000'.
- When you visit the URL, you will receive a greeting message as a response.

To run the server:
1. Navigate to the directory where the file is located.
2. Run the command: flask run
3. Visit '127.0.0.1:5000' in your web browser to see the greeting message.

This app demonstrates how to create a basic Flask application with one route and a simple response.
"""
app = Flask(__name__)

@app.route('/', methods=['GET'])  # We only need GET here for a simple greeting app
def say_hello():
    greet = "Hello MR/MISS, Welcome to the First Flask App" 
    return greet

if __name__ == '__main__':
    app.run(debug=True)  # 'debug=True' helps with error reporting during development
