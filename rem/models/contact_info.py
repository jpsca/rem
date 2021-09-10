from rem.models.base import Base, db
from rem.models.mixins import Timestamped


class ContactInfo(Base, Timestamped):
    __tablename__ = "contact_info"

    TYPES = ("url", "phone", "email")

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    type = db.Column(db.String(10))
    value = db.Column(db.String(100))
    person_id = db.Column(db.Integer, db.ForeignKey("persons.id"))

    @db.validates("type")
    def validate_type(self, _key, value):
        value = (value or '').lower()
        assert value in self.TYPES
        return value
