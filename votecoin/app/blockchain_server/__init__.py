from flask import Flask
from app.config import config


def create_app():
    app = Flask(__name__)
    app.config.from_object(config["development"])

    from app.blockchain_server.routes import server
    app.register_blueprint(server)

    return app