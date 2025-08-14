from flask import Flask, jsonify
from api.v1 import register_blueprints

def create_app():
    app = Flask(__name__)
    register_blueprints(app)

    @app.route("/")
    def home():
        return jsonify({"message": "index"}), 200

    return app
