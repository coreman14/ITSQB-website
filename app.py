import os
from urllib.parse import urlparse

from flask import Flask, jsonify, request

result = urlparse(os.environ.get("DATABASE_URL"))

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "hello world"
