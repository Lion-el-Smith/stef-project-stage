from enum import Enum


class UserExceptions(Enum):
    PLATE_NOT_FOUND = "license Plate is required"
    CAR_NOT_FOUND = "Car Not Found"
    CAR_FOUND = "Car already parked"
    ID_NOT_FOUND = "ID is required"
    APP_ALREADY_ASSIGNED = "Application is already assigned to user."
