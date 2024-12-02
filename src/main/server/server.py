from flask import Flask
from src.main.routes.route import calculator_route

app = Flask(__name__)

app.register_blueprint(calculator_route)