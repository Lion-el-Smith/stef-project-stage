import os
import sys
import importlib
from flask import Flask
from config import Flasks
import glob
from flask import request, jsonify
from src.stef_project.car_service import CarService
from pathlib import Path

home_path = Path(__file__).parent.resolve()
ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
basedir = os.path.abspath(os.path.dirname(__file__))
os.environ.update({'ROOT_PATH': ROOT_PATH})
sys.path.append(os.path.join(ROOT_PATH, 'src'))


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(basedir, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

@app.route('/')
def hello_world():
    return jsonify('Hello, World!'), 200

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
    from src import db
    db.init_app(app)
    app.run(host=Flasks.host, port=Flasks.port,debug=True)

for f in glob.glob(os.path.dirname(__file__) + "/**/*_controller.py",recursive=True):
    spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3],f)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)