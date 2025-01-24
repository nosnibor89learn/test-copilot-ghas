from flask import Flask, jsonify
import random
import os

def create_app():
    app = build_routes()
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() in ['true', '1', 't']
    app.run(debug=debug_mode)


def build_routes():

    app = Flask(__name__)

    @app.route('/home')
    def home():
        return "Hello from home"

    return app
