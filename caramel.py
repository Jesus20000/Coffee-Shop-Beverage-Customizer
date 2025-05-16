from decorator import CondimentDecorator

class Caramel(CondimentDecorator):
    def get_description(self):
        return self._beverage.get_description() + ", Caramel"

    def cost(self):
        return self._beverage.cost() + 0.7