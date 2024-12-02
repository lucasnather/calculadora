from flask import Blueprint, jsonify, request
from src.main.factories.MakeCalculator import make_calculator
from src.errors.ErrorHandler import error_handler

calculator_route = Blueprint("calculator_route", __name__)

@calculator_route.route('/api/calculator/4', methods=['POST'])
def calculator_mean_list():
    try:
        calculator_factory = make_calculator()
        response = calculator_factory.calculator(request)

        return jsonify(response), 200
    except Exception as exception:
        errors = error_handler(exception)

        return jsonify(errors['body'])