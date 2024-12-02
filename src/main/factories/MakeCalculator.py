from src.drivers.Numpy import Numpy
from src.calculator.CalculatorFour import CalculatorFour

def make_calculator(): 
        numpy = Numpy()
        calculator = CalculatorFour(numpy)
        return calculator

    