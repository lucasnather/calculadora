from src.drivers.interface.NumpyInterface import NumpyInterface
from typing import List
from numpy import mean

class Numpy(NumpyInterface):

    def mean_calculate(self, list: List[float]) -> float:
        list_mean = mean(list)
        return list_mean
