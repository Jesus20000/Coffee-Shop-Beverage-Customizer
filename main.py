from espresso import Espresso
from milk import Milk
from caramel import Caramel

def main():
    beverage = Espresso()
    print(f"Base: {beverage.get_description()} = ${beverage.cost():.2f}")

    beverage = Milk(beverage)
    beverage = Caramel(beverage)

    print(f"Final Order: {beverage.get_description()} = ${beverage.cost():.2f}")

if __name__ == "__main__":
    main()