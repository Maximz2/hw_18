from dao.directors import DirectorsDAO
from dao.genres import GenresDAO
from dao.movies import MoviesDAO
from lib.service import BaseService
from services.movies import MoviesService
from services.schemas.directors import DirectorSchema
from services.schemas.genres import GenreSchema
from services.schemas.movies import MovieSchema
from setup_db import db

movies_schema = MovieSchema()
movies_dao = MoviesDAO(db.session)
movies_service = MoviesService(movies_dao, movies_schema)

directors_schema = DirectorSchema()
directors_dao = DirectorsDAO(db.session)
directors_service = BaseService(directors_dao, directors_schema)

genres_schema = GenreSchema()
genres_dao = GenresDAO(db.session)
genres_service = BaseService(genres_dao, genres_schema)
