# ☕ Coffee Shop Beverage Customizer

This project demonstrates the **Decorator Design Pattern** in Python by simulating a coffee shop beverage system. It allows customers to build drinks like espresso or tea and dynamically customize them with ingredients like milk, caramel, and whipped cream.

---

## 🛠️ Technologies Used

- Python 3.x  
- Object-Oriented Programming  
- Decorator Design Pattern

---

## 🧠 Design Pattern: Decorator

The **Decorator Pattern** allows for behavior to be added to individual objects dynamically without affecting the behavior of other objects from the same class. This is ideal for creating customizable beverages without needing a subclass for every combination.

---

## 📁 Project Structure

- `beverage.py` – Abstract base class for all beverages  
- `espresso.py` – Concrete base class representing espresso  
- `decorator.py` – Abstract base class for all condiment decorators  
- `milk.py` – Adds milk to a beverage  
- `caramel.py` – Adds caramel to a beverage  
- `main.py` – Composes and prints final customized beverage  
- `README.md` – Project documentation

---

## 🚀 Features

- Create base beverages like espresso  
- Add ingredients dynamically using decorators  
- Calculate final cost and description  
- Simple, extendable class structure

---

## 📌 Sample Output

```

Base: Espresso = \$2.00
Final Order: Espresso, Milk, Caramel = \$3.20

````

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/yourusername/coffee-shop-beverage-customizer.git
cd coffee-shop-beverage-customizer
````

2. Run the main script:

```bash
python main.py
```
