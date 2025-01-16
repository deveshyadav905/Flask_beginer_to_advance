# Single File Flask Application

This project demonstrates the simplest way to create a Flask application, encapsulated in a single file. It serves as the foundation for beginners to understand the basics of Flask.

## Overview
- **Purpose**: To build and run a basic Flask application.
- **Features**:
  - Create a basic Flask server.
  - Define a route that returns a simple greeting.
  - Run the application locally.

## Directory Structure
```
single_file_app/
    app.py  # Contains the single-file Flask application
```

## Prerequisites
- Python (3.8 or later recommended)
- pip (Python package manager)

## Setup Instructions
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/Flask_beginer_to_advance.git
    cd Flask_beginer_to_advance/single_file_app
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
### app.py
```python
from flask import Flask

"""Starting With Single File Application
Returns:
    Server: We will start a Flask application shortly and check the first greeting from the server on localhost '127.0.0.1:5000'
    To run this server, go to the directory 'first_app/single_file_app'
    and hit the command: flask run
"""
app = Flask(__name__)

@app.route('/', methods=['GET'])  # Handles GET requests
def say_hello():
    greet = "Hello MR/MISS, Welcome to the First Flask App"
    return greet

if __name__ == '__main__':
    app.run(debug=True)  # 'debug=True' helps with error reporting during development
```
- **Flask Initialization**: `app = Flask(__name__)`
- **Route Definition**: `@app.route('/', methods=['GET'])`
- **Debug Mode**: `app.run(debug=True)` ensures that errors are displayed clearly during development.

## Expected Output
When you visit [http://127.0.0.1:5000](http://127.0.0.1:5000), you should see:
```
Hello MR/MISS, Welcome to the First Flask App
```

## Key Learning Points
- Understand how to set up a minimal Flask application.
- Learn to define routes with `@app.route`.
- Use the `debug` mode to identify and fix errors easily.

## Next Steps
Move on to more advanced ways to structure a Flask app, such as using configuration files or the factory method. Check out the `config_app` project for the next step!

