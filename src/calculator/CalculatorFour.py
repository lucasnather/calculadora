from flask import request as FlaskRequest
from src.drivers.interface.NumpyInterface import NumpyInterface
from src.errors.BadRequest import BadRequest
from src.errors.InvalidType import InvalidType
from typing import Dict, List

class CalculatorFour:

    def __init__(self, numpyInterface: NumpyInterface) -> None:
        self.numpyinterface = numpyInterface

    def calculator(self, request: FlaskRequest):
        body = request.json
        list_numbers = self.__validate_body(body)
        mean = self.__calculator_mean(list_numbers)
        mean_formatted_response = self.__formatted_response(mean)

        return mean_formatted_response

    def __validate_body(self, body: Dict):
        if 'numbers' not in body:
            raise BadRequest("Numbers not in body")
        
        if not isinstance(body['numbers'], list) or not all(isinstance(num, float) for num in body['numbers']):
            raise InvalidType("Numbers is not a list of floats")

        list_numbers = body['numbers']
        return list_numbers

    def __calculator_mean(self, list_numbers: List[float]):
        mean = self.numpyinterface.mean_calculate(list_numbers)

        return mean
    
    def __formatted_response(self, mean: float):

        return {
            "Calculator": {
                "mean": round(mean, 2)
            }
        }
