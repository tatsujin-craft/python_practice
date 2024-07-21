#!/usr/bin/env python3
"""
Script Name: class.py
Description: 
    This script calls class instance.
Usage:
    $ python3 class.py

Author: tatsujin
Date: 2024-07-20
"""


class MyClass:
    class_variable = 0

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable  # Instance variable
        MyClass.class_variable += 1  # Increment

    def instance_method(self):
        print(f"Instance variable: {self.instance_variable}")
        print(f"Class variable from instance method: {MyClass.class_variable}")

    @classmethod
    def class_method(cls):
        print(f"Class variable from class method: {cls.class_variable}")


if __name__ == "__main__":
    # create instance
    obj1 = MyClass(1)
    obj2 = MyClass(2)

    # Call instance
    obj1.instance_method()
    obj2.instance_method()

    MyClass.class_method()
