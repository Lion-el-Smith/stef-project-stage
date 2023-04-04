from src.models import *
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_migrate import Migrate
from datetime import timedelta
import os
import glob
import importlib
from flask_migrate import Migrate, upgrade, init
import cx_Oracle


app = Flask(__name__)
CORS(app)


jwt = JWTManager(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(app, metadata=metadata)
migrate = Migrate(app, db)

with app.app_context():
    if not os.path.isdir(os.path.join(os.path.dirname(os.path.dirname(__file__)), "migrations")):
        init(directory='migrations', multidb=False)
    upgrade(directory=os.path.join(os.path.dirname(
        os.path.dirname(__file__)), "migrations"))


# Dynamically add *_controller.py files to flask application
# for f in glob.glob(os.path.dirname(__file__) + "/**/*_controller.py",recursive=True):
#     spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3],f)
#     mod = importlib.util.module_from_spec(spec)
#     spec.loader.exec_module(mod)
