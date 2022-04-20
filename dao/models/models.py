from sqlalchemy.orm import relationship

from dao.models.base import BaseModel
from setup_db import db


class Genre(BaseModel):
    __tablename__ = "genre"
    name = db.Column(db.String)


class Director(BaseModel):
    __tablename__ = "director"
    name = db.Column(db.String)


class Movie(BaseModel):
    __tablename__ = "movie"
    title = db.Column(db.String(255))
    description = db.Column(db.String)
    trailer = db.Column(db.String)
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)

    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'))

    genre = relationship("Genre")
    director = relationship("Director")
