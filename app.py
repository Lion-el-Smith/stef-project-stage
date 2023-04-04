import importlib
from flask import Flask, json
from config import Flasks
import distutils
from distutils import util
import glob
import importlib
import os
from flask import request, jsonify
from src.stef_project.car_service import CarService

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/car/<license_plate>', methods=['GET'])
def get_car(license_plate):
    licenseplate= license_plate.lower()
    car= CarService().get_car(licenseplate)
    return jsonify(car), 200

@app.route('/car/<license_plate>', methods=['DELETE'])
def delete_car(license_plate):
    licenseplate= license_plate.lower()
    CarService.delete_car(licenseplate) #classes should pascal case
    return jsonify(success=True),200

    

@app.route('/car', methods=['PUT'])
def update_car():
    data= request.get_json()
    is_dirty: bool= data.get('is_dirty')
    hours_parked= data.get('hours_parked')
    car_color= (data.get('car_color')).lower()
    license_plate=(data.get('license_plate')).lower()
    car= CarService().update_car(
        license_plate,
        car_color,
        is_dirty,
        hours_parked
    )
    return jsonify(car), 200

@app.route('/car', methods=['POST'])
def add_car():
    data= request.get_json()
    is_dirty: bool= data.get('is_dirty')
    hours_parked= data.get('hours_parked')
    car_color= (data.get('car_color')).lower()
    license_plate=(data.get('license_plate')).lower()
    
    car= CarService().add_car(
        license_plate,
        car_color,
        is_dirty,
        hours_parked,
        price= 0
    )
    return jsonify(car), 200

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(host=Flasks.host, port=Flasks.port,debug=True)#sdsfubsfjhbkfbsfsfs

for f in glob.glob(os.path.dirname(__file__) + "/**/*_controller.py",recursive=True):
    spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3],f)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)