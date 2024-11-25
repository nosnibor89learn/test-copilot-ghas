from flask import Flask, jsonify
import random


def create_app():
    app = build_routes()
    app.run(debug=True)


def build_routes():

    app = Flask(__name__)

    @app.route('/home')
    def home():
        return "Hello from home"

    return app
