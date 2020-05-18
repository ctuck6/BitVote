from app.blockchain_server import create_app


app = create_app()
app.app_context().push()


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', "--port", default=5001, type=int)
    args = parser.parse_args()
    port = args.port

    app.run(host="127.0.0.1", port=port, debug=True)