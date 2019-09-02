#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:LXC
@file: pandasTest1.py
@time: 2019/08/27
"""

import pandas as pd
import numpy as np

'''
pandas中主要有两种数据结构，分别是Series和DataFrame

Series:一种类似于一维数组的对象，是由一组数据（各种Numpy类型）以及一组与之相关的数据标签（即索引）组成。
       仅由一组数据也可产生简单的Series对象，注意：Series中的索引值是可以重复的。

DataFrame:一个表格型的数据结构，包含一组有序的列，每列可以是不同的值类型（数值、字符串、布尔型等），
          DataFrame即有行索引也有列索引，可以看作是由Series组成的字典

'''

'''
#Series
#通过一维数组创建

a = np.array([1,2,3,4])
ser = pd.Series(a)
print(ser)

iex = ser.index # 通过index查看索引，也可以修改，索引可以重复
print(iex)

vls = ser.values # 通过values查看值
print(vls)

ser.index = ['数学','数学','英语','体育'] #重置索引值
print(ser)

print(ser["数学"])
print(ser["英语"])

#创建的时候设置索引值
ser2 = pd.Series(a,index = list("abcd"))
print(ser2)



#通过字典的方式创建
a = {'2017':'急急急','2018':'积极','2019':'积极解决'}
ser = pd.Series(a)
print(ser)

#Series对象本身及索引都具有name属性，默认为空，根据需要可以进行赋值操作
ser.name = "测试数据"
print(ser)

ser.index.name = "年份"
print(ser)

#常见Series的属性
# axes    返回行轴标签列表
# dtype   返回对象的数据类型
# empty   如果系列为空，则返回True
# ndim    返回底层数据的维数，默认定义：1
# size    返回基础数据中的元素数
# values  将系列作为ndarry返回
# head()  返回前n行
# tail()  返回最后n行



#Series的运算：Numpy中的数组运算，在Series中都保留了，均可以使用，并且Series进行数组运算时，索引与值之间的映射关系不会发生改变
#当多个Series对象之间进行运算的时候，如果不同series之间具有不同的索引值，那么运算会自动对其相同索引值的数据，如果某个Series没有某个索引值，
#那么最终结果会赋值为NaN

a = {'2017':'急急急11','2018':'积极11','2019':'积极解决11'}
ser = pd.Series(a)

b = {'hhh':'急急急22','mmm':'积极22','bbb':'积极解决22'}
ser2 = pd.Series(b)

print(ser + '3')
print(ser + ser2)

#Series 缺失值检测，通过isnull()和 notnull(),可通过布尔索引进行过滤

'''

