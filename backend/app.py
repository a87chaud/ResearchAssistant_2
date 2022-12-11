from flask import Flask
from flask import request, jsonify
from markupsafe import escape
import get_links
import json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def index():
    return 'Success', 200


@app.route('/cite')
def cite():
    return get_links.cite_sources("https://en.wikipedia.org/wiki/Electricity")

if __name__ == "__main__":
    app.run(debug=True)