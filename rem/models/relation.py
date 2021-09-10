from rem.models.base import Base, db
from rem.models.mixins import Timestamped


class Relation(Base, Timestamped):
    __tablename__ = "relations"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    value = db.Column(db.String(100))
    person_id = db.Column(db.Integer, db.ForeignKey("persons.id"))
    rel_person_id = db.Column(db.Integer, db.ForeignKey("persons.id"))
    rel_person = db.relationship(
        "Person",
        backref=db.backref("related"),
        lazy="select",
        foreign_keys=[rel_person_id]
    )
    person = db.relationship(
        "Person",
        backref=db.backref("relations"),
        lazy="select",
        foreign_keys=[person_id]
    )
