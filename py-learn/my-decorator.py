#!-*- coding:utf-8 -*-
__author__ = 'xinhua'

'''
函数装饰器
'''
# def decorator(F):
#
#     def new_F(a, b):
#         print("input", a, b)
#         return F(a, b)
#
#     return new_F
#
# @decorator
# def square_sum(a, b):
#     return a**2 + b**2
#
# @decorator
# def square_diff(a, b):
#     return a**2 - b**2
#
# print(square_sum(3, 4))
# print(square_diff(3, 4))


'''
类装饰器
'''
def decorator(aClass):
    class newClass:
        def __init__(self, age):
            self.total_display = 0
            self.wrapped = aClass(age)

        def display(self):
            self.total_display += 1
            print "total display", self.total_display
            self.wrapped.display()
    return newClass

@decorator
class Bird():
    def __init__(self, age):
        self.age = age

    def display(self):
        print "My age is ", self.age

eagleLord = Bird(5)
for i in range(3):
    eagleLord.display()

