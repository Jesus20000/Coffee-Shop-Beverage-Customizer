Coffee Shop Beverage Customizer - Decorator Pattern

Overview:
This project demonstrates the Decorator Design Pattern by modeling a customizable beverage system for a coffee shop. 
Instead of creating multiple subclasses for every drink combination, we use decorators to wrap base drinks with optional ingredients.

Structure:
- beverage.py: Abstract base class defining the interface for beverages.
- espresso.py: Concrete class implementing a base drink.
- decorator.py: Abstract class for all condiment decorators.
- milk.py, caramel.py: Concrete decorators that modify behavior of wrapped beverages.
- main.py: Demonstrates creating and customizing a beverage order.

How to Run:
1. Save all files in the same folder.
2. Open terminal and navigate to that folder.
3. Run the program with:

   python main.py

Expected Output:
Displays the base beverage and the final decorated order with total cost.

Example:
Base: Espresso = $2.00  
Final Order: Espresso, Milk, Caramel = $3.20

Author: Isa Zeynalov
