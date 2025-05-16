from beverage import Beverage

class Espresso(Beverage):
    def get_description(self):
        return "Espresso"

    def cost(self):
        return 2.0