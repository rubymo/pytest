# -*- coding: utf-8 -*-
# @Time    : 2021/8/9 12:00
# @Author  : Ruby
# @FileName: hello.py
# @Software: PyCharm


# print("hello world")
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
#driver.close()
#driver.quit()
