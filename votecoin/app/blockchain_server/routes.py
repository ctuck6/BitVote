from flask import Blueprint


server = Blueprint("blockchain_server", __name__)


@server.route('/', methods=["GET", "POST"])
def hello_world():
    return "Hello, World!"
