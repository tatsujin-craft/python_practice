#!/usr/bin/env python3
"""
閏年の判定プログラム
グレゴリオ暦の西暦を整数で入力

閏年判定の条件
西暦が4で割り切れる年は閏年。
ただし、100で割り切れる年は閏年ではない。
ただし、400で割り切れる年は閏年。
"""


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


year = int(input("Please enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
