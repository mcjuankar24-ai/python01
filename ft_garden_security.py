#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_security.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jmesa-ci <jmesa-ci@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/21 13:04:39 by jmesa-ci            #+#    #+#            #
#   Updated: 2026/06/02 14:51:46 by jmesa-ci           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: float, days: int):
        self.name = name
        if ((height or days) < 0):
            if (height < 0):
                print(f"{self.name.capitalize()}: Error, ", end=' ')
                print("height can't be negative")
            if (days < 0):
                print(f"{self.name.capitalize()}: Error, ", end=' ')
                print("age can't be negative")
            print("Plant creation cancelled")
        else:
            self._days = days
            self._height = height
            print(f"Plant created: {self.name.capitalize()}:", end=' ')
            print(f"{self._height}cm, {self._days} days old")

    def show(self):
        print(f"{self.name.capitalize()}: {self._height} cm,", end=' ')
        print(f"{self._days} days old", end=' ')
        print()

    def _age(self):
        self._days += 1

    def grow(self, days: int, growth: float):
        for i in range(1, days + 1):
            self._height += growth
            self._age()
            print(f"=== Day {i} ===")
            print(f"{self.name.capitalize()}:", end=' ')
            print(f"{round(self._height, 2)} cm)", end=' ')
            print(f", {self._days} days old")
        print(f"Growth this week: {round(growth*days, 2)} cm")

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


def main():
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print()
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-40.5)
    rose.set_age(-30)
    print()
    print("Current state:", end=' ')
    rose.show()


if __name__ == "__main__":
    main()
