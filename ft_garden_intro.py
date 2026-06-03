#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_intro.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jmesa-ci <jmesa-ci@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/19 12:34:15 by jmesa-ci            #+#    #+#            #
#   Updated: 2026/06/02 14:29:59 by jmesa-ci           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


def main():
    rose = Plant("Rose", 25, 30)
    print("=== Welcome to My Garden ===")
    print("Plant:", rose.name.capitalize())
    print("Height:", rose.height, "cm")
    print("Age:", rose.age, "days")
    print()
    print("=== End of Program ===")


if __name__ == "__main__":
    main()
