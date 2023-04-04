#from src.stef_project.DTO.car_DTO import carDTO
from src import app
from flask import request, jsonify
from src.stef_project.car_service import CarService


@app.route('/car-app', methods=['GET'])
def get_car():
    data = request.get_json()
    car = CarService().get_car(
        license_plate=data.get('license_plate')
    )
    return (car.__dict__), 200


@app.route('/car-app', methods=['PUT'])
def update_car():
    data = request.get_json()
    car = CarService().update_car(
        license_plate=data.get('license_plate'),
        car_color=data.get('car_color'),
        isdirty=data.get('isdirty'),
        hours_parked=data.get('hours_parked')
    )
    return (car.__dict__), 200


@app.route('/car-app/<str:license_plate>', methods=['DELETE'])
def delete_car(license_plate):
    CarService.delete_car(str(license_plate))
    return jsonify(success=True), 200


@app.route('/car-app', methods=['POST'])
def add_car():
    data = request.get_json()
    car = CarService().add_car(
        license_plate=data.get('license_plate'),
        car_color=data.get('car_color'),
        isdirty=data.get('isdirty'),
        hours_parked=data.get('hours_parked')
    )
    return (car.__dict__), 200
