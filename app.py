from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db

from views.directors import directors_ns
from views.genres import genres_ns
from views.movies import movies_ns


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.app_context().push()
    return app


def configure_app(app: Flask):
    db.init_app(app)
    db.create_all()
    api = Api(app)
    api.add_namespace(movies_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)


if __name__ == '__main__':
    app_ = create_app()
    configure_app(app_)
    app_.run(host="localhost", port=10001)
