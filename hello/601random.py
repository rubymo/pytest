# -*- coding: utf-8 -*-
# @Time    : 2021/9/23 10:10
# @Author  : Ruby
# @FileName: 601random.py.py
# @Software: PyCharm

import random
import winsound

# winsound.MessageBeep()

#
# x = random.randint(1, 100)
# i = 0
# while i < 100:
#     y = input("请输入数字：")
#     y = int(y)
#     print(x == y)
#     if x == y:
#         print("===========")
#         print("猜中啦")
#         print(y, x)
#         print("===========")
#         break
#     else:
#         print("猜错啦")
#         print(y, x)

# '''
# 练习而已
# '''
# a = 1
# print(type(a))
#
# b = 1.1
# print(type(b))
#
# c = True
# print(type(c))
#
# d = 'True'
# print(type(d))
#
# e = [4, 5, 6, 3]
# print(type(e))
#
# f = {"name": "moli", "age": 12}
# print(type(f))


# '''
# 函数/方法
# '''

# import winsound
# winsound.MessageBeep()


def fun():
    a = 5
    b = 4
    c = a + b
    d = a * b
    # print(c)
    # print(d)
    return c
    return d
    # c=1000  #赋值失败，因为return后，方法就结束了


def funB(c):
    res = c * 10
    print(res)
#
#
# '''
# 调用方法fun()
# '''
# fun()
funB(fun())


