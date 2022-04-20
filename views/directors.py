from flask_restx import Resource, Namespace

from container import directors_service
from services.schemas.directors import DirectorSchema


directors_ns = Namespace('directors')

director_schema = DirectorSchema()


@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        return directors_service.get_all()


@directors_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        return directors_service.get_one(did)
