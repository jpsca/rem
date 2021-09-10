from .base import Base, db
from .mixins import Timestamped


class Person(Base, Timestamped):
    __tablename__ = "persons"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    middle_name = db.Column(db.String(100), nullable=True)
    last_name = db.Column(db.String(100), nullable=True)
    nickname = db.Column(db.String(100), nullable=True)
    birthdate = db.Column(db.Date, nullable=True)
    estimated_age = db.Column(db.String(20), nullable=True)

    contact_info = db.relationship(
        "ContactInfo", backref=db.backref("person"), lazy="select"
    )
    addresses = db.relationship(
        "Address", backref=db.backref("person"), lazy="select"
    )

