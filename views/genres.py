from flask_restx import Resource, Namespace

from container import genres_service
from services.schemas.genres import GenreSchema


genres_ns = Namespace('genres')

genre_schema = GenreSchema()


@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        return genres_service.get_all()


@genres_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        return genres_service.get_one(gid)
