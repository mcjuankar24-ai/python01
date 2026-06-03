#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_growth.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jmesa-ci <jmesa-ci@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/19 14:20:07 by jmesa-ci            #+#    #+#            #
#   Updated: 2026/06/02 15:18:32 by jmesa-ci           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: float, days: int):
        self.name = name
        self.height = height
        self.days = days

    def show(self):
        print(f"{self.name.capitalize()}: {self.height} cm,", end=' ')
        print(f"{self.days} days old", end=' ')
        print()

    def age(self):
        self.days += 1

    def grow(self, days: int, growth: float):
        for i in range(1, days + 1):
            self.height += growth
            self.age()
            print(f"=== Day {i} ===")
            print(f"{self.name.capitalize()}:", end=' ')
            print(f"{round(self.height, 2)} cm)", end=' ')
            print(f", {self.days} days old")
        print(f"Growth this week: {round(growth*days, 2)} cm")


def main():
    rose = Plant("Rose", 25.0, 30)
    print("=== Garden Plant Growth ===")
    rose.show()
    rose.grow(7, 0.8)


if __name__ == "__main__":
    main()
