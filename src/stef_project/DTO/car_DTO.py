from dataclasses import dataclass


@dataclass
class carDTO():

    license_plate: str
    car_color: str
    is_dirty: bool
    hrs_parked: int
    price: float

    def __init__(self, license_plate, car_color, is_dirty, hours_parked, price):
        self.license_plate = license_plate
        self.car_color = car_color
        self.is_dirty = is_dirty
        self.hrs_parked = hours_parked
        self.price = price
