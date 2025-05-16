from decorator import CondimentDecorator

class Milk(CondimentDecorator):
    def get_description(self):
        return self._beverage.get_description() + ", Milk"

    def cost(self):
        return self._beverage.cost() + 0.5