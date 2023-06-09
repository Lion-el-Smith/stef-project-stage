from src.models.car_model import CarModel, db
from src.stef_project.DTO.car_DTO import carDTO


class CarRepo():
    def __init__(self):
        self.db = db

    def add_car(self, license_plate, car_color, is_dirty, hrs_parked, Price) -> None:
        new_car = CarModel(license_plate=license_plate,
                           is_dirty=is_dirty,
                           car_color=car_color,
                           hours_parked=hrs_parked,
                           Price=Price
                           )
        self.db.session.add(new_car)
        self.db.session.commit()
        car_DTO = carDTO(new_car.license_plate, new_car.car_color, new_car.is_dirty, new_car.hrs_parked, new_car.price)
        return car_DTO

    def update_car(self, license_plate, car_color, is_dirty, hours_parked,  price):
        car = CarModel.query.filter(
            CarModel.license_plate == license_plate).first()
        car.is_dirty = is_dirty
        car.car_color = car_color
        car.hrs_parked = hours_parked
        car.price = price
        db.session.add(car)
        db.session.commit()
        car_DTO = carDTO(car.license_plate, car.car_color, car.is_dirty, car.hrs_parked, car.price)
        return car_DTO

    def remove_car(self, license_plate) -> None:
        car = CarModel.query.filter(
            CarModel.license_plate == license_plate).delete()
        self.db.session.commit()

    def find_car(self, license_plate) -> carDTO:
        car: CarModel = CarModel.query.filter(
            CarModel.license_plate == license_plate).first()
        car_DTO = carDTO(car.license_plate, car.car_color,
                         car.is_dirty, car.hrs_parked, car.price)
        return car_DTO
