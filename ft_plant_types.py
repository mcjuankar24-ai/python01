#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_types.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jmesa-ci <jmesa-ci@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/22 11:25:58 by jmesa-ci            #+#    #+#            #
#   Updated: 2026/06/02 15:18:35 by jmesa-ci           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: float, days: int):
        self.name = name
        if ((height or days) < 0):
            if (height < 0):
                print(f"{self.name.capitalize()}: Error,", end=' ')
                print("height can't be negative")
            if (days < 0):
                print(f"{self.name.capitalize()}: Error,", end=' ')
                print("age can't be negative")
            print("Plant creation cancelled")
        else:
            self._days = days
            self._height = height

    def show(self):
        print(f"{self.name.capitalize()}: {round(self._height)} cm,", end=' ')
        print(f"{self._days} days old", end=' ')
        print()

    def _age(self):
        self._days += 1

    def _grow(self, days: int, growth: float):
        for i in range(1, days + 1):
            self._height += growth
            self._age()

    def set_height(self, height: float):
        if (height < 0):
            print(f"{self.name.capitalize()}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
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


class Flower(Plant):
    def __init__(self, name: str, height: float, days: int, color: str):
        super().__init__(name, height, days)
        self.color = color
        self.bloomed = False

    def bloom(self):
        print(f"[asking the {self.name} to bloom]")
        self.bloomed = True

    def show(self):
        super().show()
        print(f" Color: {self.color}")
        if (self.bloomed is True):
            print(f" {self.name.capitalize()} is blooming beautifully!")
        else:
            print(f" {self.name.capitalize()} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, days: int, diam: float):
        super().__init__(name, height, days)
        self.trunk_diameter = diam

    def produce_shade(self):
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name.capitalize()} now", end=' ')
        print(f"produces a shade of {self._height}cm", end=' ')
        print(f"long and {self.trunk_diameter}cm wide.")

    def show(self):
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, days: int, month: str):
        super().__init__(name, height, days)
        self.harvest_season = month
        self.nutritional_value = 0

    def _grow(self, days: int, growth: float):
        super()._grow(days, growth)
        print(f"[make {self.name} grow and age for {days} days]")
        self.nutritional_value += days

    def show(self):
        super().show()
        print(f" Harvest season: {self.harvest_season.capitalize()}")
        print(f" Nutritional value: {self.nutritional_value}")


def main():
    rose = Flower("Rose", 15.0, 10, "red")
    print("=== Garden Plant Types ===")
    print("== Flower")
    rose.show()
    rose.bloom()
    rose.show()
    print()
    print("== Tree")
    oak = Tree("oak", 200.0, 365, 5.0)
    oak.show()
    oak.produce_shade()
    print()
    print("== Vegetable")
    tomato = Vegetable("tomato", 5, 10, "April")
    tomato.show()
    tomato._grow(20, 2.1)
    tomato.show()


if __name__ == "__main__":
    main()
