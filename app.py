from flask import Flask, jsonify
import random


def create_app():
    app = build_routes()
    app.run(debug=True)


def build_routes():

    app = Flask(__name__)

    @app.route('/201')
    def hello201():
        return "Hello, course 201!"

    @app.route('/random-boolean')
    def random_boolean():
        value = random.choice([True, False])
        return jsonify(result=value)

    # Route (/201/cat)
    @app.route('/201/cat')
    def cat():
        dummy_data = {"name": "Whiskers", "age": 3,
                      "breed": "Siamese", "color": "Brown"}
        response = jsonify(dummy_data)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    return app
