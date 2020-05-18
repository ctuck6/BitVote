from flask import Flask
from app.config import config


def create_app():
    app = Flask(__name__)
    app.config.from_object(config["development"])


    from app.blockchain_client.routes import client
    app.register_blueprint(client)

    return app