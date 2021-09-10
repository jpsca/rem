from rem.models.base import Base, db
from rem.models.mixins import Timestamped


class Address(Base, Timestamped):
    __tablename__ = "addresses"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    country = db.Column(db.String(20))
    region = db.Column(db.String(20))
    value = db.Column(db.Text)
    person_id = db.Column(db.Integer, db.ForeignKey("persons.id"))
