#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:LXC
@file: pandasTest3.py
@time: 2019/09/05
"""

import pandas as pd

'''
pandas基本功能
（1）数据文件读取/文本数据读取与文本储存
（2）索引、选取和数据过滤
（3）算法运算和数据对齐
（4）函数的运用
（5）层次索引
（6）排序
（7）时间序列
（8）数据合并
（9）分组聚合
（10）数据透视

'''

#（1）数据文件读取/文本数据读取与文本储存：通过pandas提供的read_xxx相关函数可以读取文件中的数据，并形成DataFrame，常用的数据读取方法：read_csv，主要可以读取文本类型数据
#                                        通过to_xxx相关函数进行数据的保存
#数据读取
pf = pd.read_csv("../file/pandansReadTest.csv")  #读取csv文件
print(pf)

pf2 = pd.read_excel("../file/panReadTest2.xlsx")  #读取excel
print(pf2)

pf3 = pd.read_csv("../file/panReadTest3.txt")  #读取txt文件，默认以逗号分割，可通过seq指定分隔符，header如果设置为None则不去读头部
print(pf3)

#数据保存
pf3.to_csv("../file/saveTest4.txt",encoding = "utf-8",index = None) # 保存时设置不要默认的index,前面就不会多出来默认的index
print(pd.read_csv("../file/saveTest4.txt"))

pf3.to_excel("../file/saveTest5.xlsx",encoding = "utf-8",index = None)

pf2.to_csv("../file/saveTest4.txt",encoding = "utf-8",index = None)



