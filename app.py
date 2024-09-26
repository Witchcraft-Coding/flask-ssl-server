from flask import Flask
from os import environ as env

from config import port, debug, ssl_context

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(port=(env.get('PORT', port)), debug=debug, ssl_context=(None if env.get('SSL') != 'true' else ssl_context))