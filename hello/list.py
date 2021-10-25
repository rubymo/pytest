# -*- coding: utf-8 -*-
# @Time    : 2021/9/23 10:05
# @Author  : Ruby
# @FileName: list.py.py
# @Software: PyCharm

'''
列表的应用场景(有序序列)，
序列中，每个元素都有属于自己的编号（索引）。

string类型的数据只有一个维度
列表初始化
列表的赋值
in运算
添加
    append：向列表中添加一个对象object
    insert
    extend：拼接两个列表
提取元素
    通过下标提取值
    通过值提取下标
遍历列表、len、range
修改元素
删除
    pop删除下标
    remove，指定串


'''
# response  = "Ruben Allen,28,m;Linda Hardy,30,f,Lindsey Cook,29,f"

# 变量使用前需要赋值
# List=[]#列表的初始化
# List=['a','b','c']#列表的赋值

# in运算符判断
# list=['tom','lily','rose']
# print('lily'in list)

# List.append('naw')
# List.insert(0,'bull')
# list.extend('abc')
# print(list)
# list.extend(['abc','efg'])
# print(list)

# # 通过下标提取
# name_list=['tom','lily','rose']
# print(name_list[0])  # tom
# print(name_list[1])	#lily
# print(name_list[-1])  # rose
# # 通过值提取下标
# name_list = ['tom','lily','rose']
# print(name_list.index('rose'))

# # 统计重复
# name_list=['tom','lily','rose','tom']
# print(name_list.count('tom'))

# 通过下标修改
# name_list=['tom','lily','rose','tom']
# name_list[-2]='shamo'
# print(name_list)

name_list=['tom','lily','rose','tom']
# 方式1,list是可迭代对象
# for i in name_list:
#     print('i:',i,' type:',type(i))

# 方式2，使用len函数和下标(多一个维度)
for i in range(len(name_list)):
    print('i:',i,' name_list:',name_list[i])

# 删除
# pop函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
# name_list=['tom','lily','rose']
# del_name=name_list.pop(0)#返回的是被删除的元素#结果是tom
# print('del_name=name_list.pop(0):',del_name)
# print(name_list)


# #不加索引，默认删除最后一个元素
# name_list.pop()
# #结果是['lily']
# print('name_list:',name_list)

# name_list=['tom','lily','rose']
# del name_list[-1]
# print(name_list)
# del name_list
# print(name_list)

# 移除列表中某个值的第一个匹配项
# aList = [123, 'xyz', 'zara', 'abc', 'xyz']
# aList.remove('xyz')
# print ("List : ", aList)

# 清空列表
# l=['tom','lily','rose']
# l.clear() #清空值
# del l #删除变量引用
# print(l)


# reverse翻转，
# name_list.reverse()
# print(name_list)

# sort排序
# li = [1,34,67,2,10]
# li.sort()  # 默认升序
# li.sort(reverse=True)  # 降序
# print(li)
# name_list.sort()
# print(name_list)


# 会改变列表的顺序----去重---
# li = [9,9,1,1,2,3,3,3,3,5,7,]
# new_li = list(set(li))
# #按照原来的索引位置排序 key:指明一个排序的规则
# new_li.sort(key=li.index)
# print(new_li)