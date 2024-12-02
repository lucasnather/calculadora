from abc import abstractclassmethod, ABC
from typing import List

class NumpyInterface(ABC):

    @abstractclassmethod
    def mean_calculate(self, list: List[float]) -> float:
        pass