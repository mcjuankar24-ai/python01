<p align="center">
  <img src="https://img.shields.io/badge/Language-Python%203.10%2B-blue?style=for-the-badge&logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/Paradigm-OOP-red?style=for-the-badge" alt="OOP Paradigm">
  <img src="https://img.shields.io/badge/Linter-Flake8-green?style=for-the-badge" alt="Flake8 Standard">
  <img src="https://img.shields.io/badge/Type%20Checking-Mypy-orange?style=for-the-badge" alt="Mypy Checked">
</p>

# Code Cultivation - Object-Oriented Garden Systems

**42 Málaga** | **Author:** jmesa-ci
**Version:** 3.2

## 📖 Summary

Build a comprehensive digital garden ecosystem while discovering advanced Python
concepts. This project progresses from basic Python program structure to full
Object-Oriented Programming, creating tools to manage community gardens through
data-driven approaches.

Each exercise builds on the previous one, culminating in a complete digital garden
ecosystem that models plants, their growth, their protection against invalid data,
their specialization into types (Flower, Tree, Vegetable, Seed), and analytics
about their behavior over time.

## 🛠 Requirements

- Python 3.10+
- Code respects `flake8` linter standards
- All functions and methods include type hints (checked with `mypy`)
- Naming conventions: classes in `PascalCase`, functions/variables in `snake_case`

## 📂 Project Structure

```
.
├── ex0/
│   └── ft_garden_intro.py       # Exercise 0: Planting Your First Seed
├── ex1/
│   └── ft_garden_data.py        # Exercise 1: Garden Data Organizer
├── ex2/
│   └── ft_plant_growth.py       # Exercise 2: Plant Growth Simulator
├── ex3/
│   └── ft_plant_factory.py      # Exercise 3: Plant Factory
├── ex4/
│   └── ft_garden_security.py    # Exercise 4: Garden Security System
├── ex5/
│   └── ft_plant_types.py        # Exercise 5: Specialized Plant Types
├── ex6/
│   └── ft_garden_analytics.py   # Exercise 6: Garden Analytics
└── README.md
```

## 🌱 Exercises

### Exercise 0 — Planting Your First Seed (`ft_garden_intro.py`)
Introduces the basic structure of a Python program: the `if __name__ == "__main__":`
entry point, simple variables, and `print()` to display information about a plant
(name, height, age).

### Exercise 1 — Garden Data Organizer (`ft_garden_data.py`)
Introduces the `Plant` class as a model for any plant. Instantiates several plants
with their own attributes (`name`, `height`, `age`) and displays them using a
`show()` method.

### Exercise 2 — Plant Growth Simulator (`ft_plant_growth.py`)
Extends `Plant` with behaviors: `age()` increments the plant's age, and `grow()`
simulates growth over a number of days, printing the state day by day and a
weekly growth summary.

### Exercise 3 — Plant Factory (`ft_plant_factory.py`)
Streamlines plant creation via the constructor (`__init__`), allowing plants to be
instantiated and initialized in a single step. At least 5 different plants are
created and displayed.

### Exercise 4 — Garden Security System (`ft_garden_security.py`)
Introduces encapsulation using the protected attribute convention (`_height`,
`_days`). Adds `get_height()`, `get_age()`, `set_height()`, and `set_age()` with
validation to prevent negative values, printing error messages and rejecting
invalid updates instead of corrupting the plant's state.

### Exercise 5 — Specialized Plant Types (`ft_plant_types.py`)
Introduces inheritance. Three specialized classes extend `Plant`:
- **Flower**: adds a `color` attribute and a `bloom()` method.
- **Tree**: adds a `trunk_diameter` attribute and a `produce_shade()` method.
- **Vegetable**: adds `harvest_season` and `nutritional_value`, which increases
  as the vegetable grows and ages.

Each subclass reuses parent behavior through `super()`, including in `__init__()`
and `show()`.

### Exercise 6 — Garden Analytics (`ft_garden_analytics.py`)
Brings every previous concept together:
- A `@staticmethod` (`is_age`) checks whether a given age is older than a year.
- A `@classmethod` (`anonymous`) creates a placeholder plant with default values.
- A `Seed` class inherits from `Flower` and tracks the number of seeds produced
  once bloomed.
- Each `Plant` tracks internal statistics (number of `grow()`, `age()`, and
  `show()` calls) — `Tree` additionally tracks `produce_shade()` calls.
- A standalone function (outside any class) displays statistics for any plant.

## ▶️ Usage

Each exercise can be run independently:

```bash
python3 ex0/ft_garden_intro.py
python3 ex1/ft_garden_data.py
python3 ex2/ft_plant_growth.py
python3 ex3/ft_plant_factory.py
python3 ex4/ft_garden_security.py
python3 ex5/ft_plant_types.py
python3 ex6/ft_garden_analytics.py
```

## ✅ Checks

```bash
flake8 .
mypy .
```

## 🤖 AI Usage Notice

In line with the project's AI Instructions chapter, any AI-assisted code in this
repository was reviewed, tested, and fully understood before submission. AI was
used to reduce repetitive tasks and support learning, not to replace understanding
of the underlying object-oriented concepts (encapsulation, inheritance, static and
class methods, nested classes).
