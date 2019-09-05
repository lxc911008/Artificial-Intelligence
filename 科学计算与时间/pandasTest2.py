#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:LXC
@file: pandasTest2.py
@time: 2019/09/02
"""

import pandas as pd

'''
#DataFrame
#DataFrame是二维数据结构，即数据以行和列的表格方式排列
#功能特点：
#  潜在的列是不同的类型
#  大小可变
#  标记轴（行和列）
#  可以对行和列执行算术运算
#DataFrame构造函数：pandas.DataFrame(data,index,columns,dtype,copy)
#  data:数据采取各种形式，如ndarry,series,map,lists,dict,constant和另一个DataFrame
#  index:对于行标签，如果没有传递索引值，默认np.arrange(n)
#  columns:对于列标签，如果没有传递索引值，默认np.arrange(n)
#  dtype:每列的数据类型
#  copy:默认值为False,此命令用于复制数据

#通过二维数组创建
arr = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
df = pd.DataFrame(arr)
print(df)

print(df.index)
print(df.columns)
print(df.values)

df = pd.DataFrame(arr,index = list('qwer'),columns = list('ASD'))
print(df)

#通过字典创建，每个key,value为每一列的数据
dict = {'a':[1,2,3], 'b':[4,5,6],'c':[7,8,9]}
df2 = pd.DataFrame(dict,index = list('DEF'))
print(df2)

#通过index,columns 可以重置行列索引,reset_index,reset_columns,删除行列索引
df2.index = ['k','v','d']
print(df2)



#索引对象：
#不管是Series还是DataFrame对象，都有索引对象
#索引对象负责管理轴标签和其他元数据
#通过索引可以从Series,DataFrame中获取值或者对某个索引值进行重新赋值
#Series或者DataFrame的自动对齐功能是通过索引实现的

arr = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

df = pd.DataFrame(arr,index = list('qwer'),columns = list('ASD'))
print(df)

#数据获取：
#列数据获取:直接通过列索引获取
#行数据获取：需要通过ix方法获取对应行索引数据，ix为旧方法，一般使用loc、iloc


print(df['S'])  #获取一列
print(df[['A','D']])  #获取两列

df['G'] = [6,7,8,10] #增加列，也可以修改列，
print(df)

df.pop('S') #列删除
print(df)

#行操作
print(df.loc['q']) #获取一行
print(df.loc[['q','e']]) #获取多行
print(df.loc[['q','e'],['A','G']]) #获取多行多列

#类似可进行行添加，行修改，通过drop可进行行删除
df = df.drop('q')  #需要重新赋值，行删除不会更新原数组
print(df)

'''


