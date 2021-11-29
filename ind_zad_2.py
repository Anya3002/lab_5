#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# индивидуальное задание №2. Написать функцию произведения положительных аргументов.

def multiply(*args):
    z = 1
    for num in args:
        z *= num
    print(z)


if __name__ == "__main__":
    multiply(5, 5)
    multiply(8, 9)
    multiply(2, 3, 7)
    multiply(3, 1, 10, 6)


