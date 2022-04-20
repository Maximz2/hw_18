from flask import request
from flask_restx import Resource, Namespace
from marshmallow import ValidationError

from container import movies_service
from services.schemas.movies import MovieSchema


movies_ns = Namespace('movies')

movie_schema = MovieSchema()


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        args = request.args
        if 'director_id' in args:
            return movies_service.get_by_director_id(args['director_id'])

        if 'genre_id' in args:
            return movies_service.get_by_genre_id(args['genre_id'])

        if 'year' in args:
            return movies_service.get_by_year(args['year'])

        return movies_service.get_all()

    def post(self):
        return movies_service.create(request.json)


@movies_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        return movies_service.get_one(mid)

    def put(self, mid):
        try:
            return movies_service.update(mid, request.json), 204
        except ValidationError as e:
            return {'errors': e.normalized_messages()}, 400

    def delete(self, mid):
        return movies_service.delete(mid)
