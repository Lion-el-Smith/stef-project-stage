import sqlite3
from db import db


class CarModel(db.Model):
    __tablename__ = 'cars'

    license_plate = db.Column(
        db.String,
        primary_key=True,
        nullable=False,
        unique=True

    )
    car_color = db.Column(
        db.String,

    )
    is_dirty = db.Column(
        db.Boolean,
        default=False,
        nullable=False,
        index=False,
    )
    hrs_parked = db.Column(
        db.Integer,
        nullable=False,
        index=False
    )
    price = db.Column(
        db.Float,
        unique=False,
        nullable=False,
        index=False,
    )

    def __init__(self, license_plate, car_color, is_dirty, hours_parked, Price):
        self.license_plate = license_plate
        self.car_color = car_color
        self.is_dirty = is_dirty
        self.hrs_parked = hours_parked
        self.Price = Price
