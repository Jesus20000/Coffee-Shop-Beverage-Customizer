from beverage import Beverage
from abc import ABC

class CondimentDecorator(Beverage, ABC):
    def __init__(self, beverage: Beverage):
        self._beverage = beverage