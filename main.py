# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#!/usr/bin/python
# -*- coding: UTF-8 -*-
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



# Press the green button in the gutter to run the script.
if __name__ == '__main__1':
    print_hi('PyCharm')
print_hi('PyCharm1')

cont = 1
string = '123'
mile = 100.2
list_ = []
for item in ['banner', 'apple', 'origin']:
    list_.append(item+'item')
    print('我在吃: ', item)
print('hello world')
print(list_)
# 元组
arr = (1, 2, 3, 4)
for index in range(len(arr)):
    print(arr[index])

import time  # 引入time模块

# 时间
print("时间戳: ", time.time())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# 函数
def fun(str):
    print('函数输出', str)
    return
fun('我是值')

#  模块
import  util
util.util('哈哈')

strq = input("请输入：")
print("你输入的内容是: ", strq)

open('test.txt')