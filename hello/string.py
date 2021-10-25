# -*- coding: utf-8 -*-
# @Time    : 2021/9/23 10:07
# @Author  : Ruby
# @FileName: string.py.py
# @Software: PyCharm

'''学习目标
    字符串的赋值
    字符串格式化输出
    字符串拼接
    公共方法
        字符串长度
        切片
        遍历字符串
    常用方法
        字符串分割
        字符串查找
        字符串替换

'''
# 1.字符串的赋值
# 单引号
# var='String'

# print (var)
# print(type(var))
# # 当我的文本串中，需要用到引号的时候。那么就会产生歧义。这时候使用单、双引号混用
# # var="今天天气"晴""
# var="今天天气'晴'"
# print(var)

# # 三引号,可以支持文本换行
# var='''天气：晴朗
# 微风
# '''
# print(var)

# *转义符
'''转义字符	描述
\(在行尾时)	续行符
\\	反斜杠符号
\'	单引号
\"	双引号
\b	退格(Backspace)
\n	换行
\t	横向制表符
\r	回车
'''

# var='\'你好\'\n我好 \r 大家好'
# print (var)

# 练习题
# 显示倒计时
# import time
# for i in range(10):
#     # print("\r离程序退出还剩%s秒" % (9-i), end="")
#     time.sleep(1)

# # 进度条功能
# import time

# for i in range(10):
#     print("\r" + "■"*i, sep="", end="")
#     # print("■"*i, sep="", end="")
#     time.sleep(0.2)
# print("\n下载完成")

# 通过input()方法为变量赋值
# name=input('请输入字母：')
# print(type(name))

# 格式化输出
# 1.使用%，使用范例 '***%类型***' %值。
# %d          整数
# %f (%.2f)   浮点数
# %s          字符串

# var=('今天是5月份的第%d周' %4)
# print(var)

# var=('鸡蛋售价%.2f' %9.888)
# print(var)
#
# # 2.使用format
# # 使用大括号‘{}’作为特殊字符代替‘%’
# # 用法1，按照顺序填充
# var=('今天是{}月份的第{}周'.format(5,4))
# print(var)

# # 用法2，按照索引填充*标号从0开始算
# var=('今天是{0}月份的第{1}周'.format(5,4))
# print(var)

# # 用法3，使用变量名
# month=5
# week=4
# var=('今天是{month}月份的第{week}周'.format(month=month,week=week))
# print(var)

# # 练习题
# #九九乘法表
# def multiplication():
#     for i in range(1,10):
#         for j in range(1,i+1):
#             print ('{}x{}={}\t'.format(j,i,i*j),end='')
#         print()

# multiplication()

# 3.Python3.6新增了f''
# month=3
# week=4
# var=f'今天是{month}月{week}日'
# print(var)

# # 字符串拼接
# # 方式1，使用加号.各个变量或者元素必须是字符串类型
# var1='字符串'
# var2='方法'
# print(var1+var2)
# var3=10086
# print(var1+var2+var3)
# #两个方案，1换拼接方法 2.对非字符串变量进行转化
# # 不恰当的方式，
# var1='字符串','拼接'
# print(var1)
# print(type(var1))
# 方式2使用join关键字
# 分隔符.join(要连接的变量)

# var=['我是','一个','列表']
# # 单纯连接
# print(type(var))
# var=''.join(var)
# print(type(var))
# print(var)

# var='***'.join(var)
# print(type(var))
# print(var)

# s='2'
# s1='o'
# v=s,s1
# print(''.join(v))

# 公共方法
# len方法,返回值是这个字符串的字“长度”
# var='一个字符串变量'
# print(type(var))

# # 遍历字符串
# for i in var:
#     if i=='一':
#         print('数量1')
#     print(i)


# 切片，是对操作对象截取的通用操作。字符串、列表、元组都支持
# 序列[开始位置下标:结束位置下标:步长]
# var="12345678"
# print(var[1])
# #为啥结果是2
# # 取偶数
# x = var[::2]
# # 提问，为啥

# # 取奇数
# x = var[1::2]

# 反转
# print(var[::-1])

# 练习题
# 取4、5、6

# var="12345678"
# 练习
# print(var[3:5:-1])

# #字符串分割
# response  = "name:Ruben Allen,name:Linda Hardy,name:Lindsey Cook"

# print (response.split(','))   # 以 i 为分隔符

# url='https://blog.csdn.net/qq_24407657/article/details/80265217'

# 字符串查找
# s1 = "我是一个接口的返回结果，name=je，age=20"
# s2 = "exam";

# print(s1.find(s2))
# print(s1.find(s2, 5))
# print(s1.find(s2, 10))


# #字符串替换
# s = "www.testfan.cn"
# print("旧地址：", s)
# print("码同学地址：", s.replace("testfan.cn", "mtongxue.com"))

# s = "这是一个s.replace例子"
# print(s.replace("是", "不是", 4))