from tests.mock_car_wash_repo import MockCarWashRepo
from werkzeug.exceptions import BadRequest
from src.stef_project.DTO.car_DTO import carDTO
from src.stef_project.enums.exceptionMessages import UserExceptions
from src.stef_project.car_service import CarService
import unittest


class MockCarWashService(unittest.TestCase):
    def __init__(self) -> None:
        self.car_service = CarService()
        self.car_service.repo = MockCarWashRepo()
        self.license_plate = "ad4569"
        self.car_color = "green"
        self.is_dirty = False
        self.hours_parked = 12
        self.price = 0
   
    # def square(self, n:int):
    #     return n*n

    # def test_square(self, n:int):
    #     n=2
    #     self.assertEquals(self.square(n), 4)

    # add requests
    # def test_add_car(self):
    #     self.license_plate = "AF5687"
    #     self.car_color = "Beige"
    #     self.is_dirty = True
    #     self.hours_parked = 8
    #     self.assertIsNot(
    #         self.car_service.add_car(
    #             self.license_plate,
    #             self.car_color,
    #             self.is_dirty,
    #             self.hours_parked,
    #         ),
    #         None)
    #     print(self.car_color)


if __name__ == '__main__':
    unittest.main()
