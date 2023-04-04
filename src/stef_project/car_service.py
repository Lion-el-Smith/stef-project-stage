from src import app
from flask import request, jsonify, request
from werkzeug.exceptions import BadRequest
from src.stef_project.DTO.car_DTO import carDTO
from src.stef_project.enums.exceptionMessages import UserExceptions
from src.stef_project.car_repo import CarRepo


class CarService():
    def __init__(self):
        self.repo = CarRepo()
        self.colors = ['red', 'green', 'black']

    def get_price(self, hours_parked, car_color, is_dirty):
        rate = 7
        price = hours_parked*rate
        if car_color in self.colors:
            price = 0.2
            if is_dirty == True:
                price = (rate*hours_parked)/2
        else:
            price = hours_parked*rate
            if is_dirty == True:
                price = (rate*hours_parked)*2
        return price

    def add_car(self, license_plate: str, car_color: str, is_dirty: bool, hours_parked: int, price: int):
        price = self.get_price(hours_parked, car_color, is_dirty)
        car: carDTO = self.repo.add_car(
            license_plate, car_color, is_dirty, hours_parked, price)
        return car

    def delete_car(license_plate):
        if not license_plate:
            raise BadRequest(UserExceptions.PLATE_NOT_FOUND.value)
        CarRepo.remove_car(license_plate)

    def update_car(self, license_plate: str, car_color: str, is_dirty: bool, hours_parked: int):
        price = self.get_price(hours_parked, car_color, is_dirty)
        car: carDTO = self.repo.update_car(
            license_plate, car_color, is_dirty, hours_parked, price)
        return car

    def get_car(self, license_plate) -> carDTO:
        if not license_plate:
            raise BadRequest(UserExceptions.PLATE_NOT_FOUND.value)
        car: carDTO = self.repo.find_car(license_plate)
        if not car:
            raise BadRequest(UserExceptions.CAR_NOT_FOUND.value)
        return car
