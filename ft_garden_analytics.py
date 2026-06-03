#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_analytics.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jmesa-ci <jmesa-ci@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/22 12:52:05 by jmesa-ci            #+#    #+#            #
#   Updated: 2026/06/02 15:17:31 by jmesa-ci           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: float, days: int):
        self.name = name
        if (height < 0 or days < 0):
            if (height < 0):
                print(f"{self.name.capitalize()}: ", end=' ')
                print("Error, height can't be negative")
            if (days < 0):
                print(f"{self.name.capitalize()}: ", end=' ')
                print("Error, age can't be negative")
            print("Plant creation cancelled")
        else:
            self.cont_grow = 0
            self.cont_age = 0
            self.cont_show = 0
            self._days = days
            self._height = height

    @staticmethod
    def is_age(days: int):
        older = False
        print(f"Is {days} days more than a year? ->", end=' ')
        if (days > 365):
            older = True
        print(older)

    @classmethod
    def anonymous(cls: type["Plant"]):
        return cls(name="Unknown plant", height=0.0, days=0)

    def show(self):
        print(f"{self.name.capitalize()}: {round(self._height)} cm,", end=' ')
        print(f"{self._days} days old", end=' ')
        print()
        self.cont_show += 1

    def _age(self, days: int):
        self._days += days
        self.cont_age += 1

    def _grow(self, days: int, growth: float):
        for i in range(1, days + 1):
            self._height += growth
        self.cont_grow += 1
        self._age(20)

    def set_height(self, height: float):
        if (height < 0):
            print(f"{self.name.capitalize()}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            self.cont_grow += 1
            print(f"Height updated: {self._height}cm")

    def set_age(self, age: int):
        if (age < 0):
            print(f"{self.name.capitalize()}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._days = age
            print(f"Age updated: {self._days} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days

    def statistics(self):
        print(f"[statistics for {self.name.capitalize()}]")
        print(f"Stats: {self.cont_grow} grow, {self.cont_age}", end=' ')
        print(f"age, {self.cont_show} show")


class Flower(Plant):
    def __init__(self, name: str, height: float, days: int, color: str):
        super().__init__(name, height, days)
        self.color = color
        self.bloomed = False

    def bloom(self):
        self.bloomed = True

    def show(self):
        super().show()
        print(f" Color: {self.color}")
        if (self.bloomed is True):
            print(f" {self.name.capitalize()} is blooming beautifully!")
        else:
            print(f" {self.name.capitalize()} has not bloomed yet")

    def _grow(self, days: int, growth: float):
        super()._grow(days, growth)


class Tree(Plant):
    def __init__(self, name: str, height: float, days: int, diam: float):
        super().__init__(name, height, days)
        self.trunk_diameter = diam
        self.cont_shade = 0

    def produce_shade(self):
        print(f"Tree {self.name.capitalize()} now produces", end=' ')
        print(f"a shade of {self._height}cm long and", end=' ')
        print(f"{self.trunk_diameter}cm wide.")
        self.cont_shade += 1

    def show(self):
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def statistics(self):
        super().statistics()
        print(f"{self.cont_shade} shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, days: int, month: str):
        super().__init__(name, height, days)
        self.harvest_season = month
        self.nutritional_value = 0

    def _grow(self, days: int, growth: float):
        super()._grow(days, growth)
        self.nutritional_value += days

    def show(self):
        super().show()
        print(f" Harvest season: {self.harvest_season.capitalize()}")
        print(f" Nutritional value: {self.nutritional_value}")


class Seed(Flower):
    def __init__(self, name, height, days, color):
        super().__init__(name, height, days, color)
        self.seeds_number = 0

    def bloom(self):
        super().bloom()
        self.seeds_number = 42

    def _grow(self, days: int, growth: float):
        super()._grow(days, growth)

    def show(self):
        super().show()
        print(f" Seeds: {self.seeds_number}")


def main():
    print("=== Garden Statistics ===")
    print("=== Check year-old ===")
    Plant.is_age(30)
    Plant.is_age(400)
    print()
    print("=== Flower")
    rose = Flower("rose", 15.0, 10, "red")
    rose.show()
    rose.statistics()
    print("[asking the rose to grow and bloom]")
    rose.set_height(23.0)
    rose.bloom()
    rose.show()
    rose.statistics()
    print()
    print("=== Tree")
    oak = Tree("oak", 200.0, 365, 5.0)
    oak.show()
    oak.statistics()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    oak.statistics()
    print()
    print("=== Seed")
    sunflower = Seed("sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower._grow(20, 1.5)
    sunflower.bloom()
    sunflower.show()
    sunflower.statistics()
    print()
    print("=== Anonymous")
    anon = Plant.anonymous()
    anon.show()
    anon.statistics()


if __name__ == "__main__":
    main()
