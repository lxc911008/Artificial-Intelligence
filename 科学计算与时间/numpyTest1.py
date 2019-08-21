#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:LXC
@file: numpyTest1.py
@time: 2019/08/18
"""

import numpy as np

#数组的创建、属性、形状改变

'''
# 创建ndarray
# 1.一维列表创建数组
li = [1,2,3,4,5]
arr = np.array(li)
print(arr)
print(type(li))
print(type(arr))

# 2.一维元组创建数组
# 3.二维列表创建数组

li = [[1,2,3,4,5],
      [6,7,8,9,10]]

arr = np.array(li)
print(arr)


# 4.创建指定长度的全零数组
zer = np.zeros(8)
print(zer)

zer2 = np.zeros((3,3)) # 创建3行3列的二维全零数组
print(zer2)


# 5.创建指定长度的全1数组
ons = np.ones(8)
print(ons)

ons2 = np.ones((3,4))
print(ons2)



# 6.创建指定长度的未初始化数组
emp = np.empty(8)
print(emp)

emp2 = np.empty((3,5))
print(emp2)



# 7.arange函数:类似python的range函数，通过指定开始值、终值和步长来创建一个一维数组，注意：最终创建的数组不包含终值
ar = np.arange(1,7)
print(ar)

ar2 = np.arange(1,7,2)
print(ar2)

ar3 = np.arange(10,0,-1)
print(ar3)



# 8.linspace函数：通过指定开始值、终值和元素个数来创建一个一维数组，数组的数据元素符合等差数列，可以通过endpoint关键字指定是否包含终值，默认包含终值
lis = np.linspace(1,8,6)
print(lis)

lis2 = np.linspace(1,8,6,endpoint=False)
print(lis2)


# 9.logspace函数：和linspace函数类似，不过创建的是等比数组，通过base指定底数
lgs = np.logspace(1,8,4,base=3,endpoint=False)
print(lgs)



# 10.random中的random函数：使用0-1之间的随机数填充数组，数组包含数量由参数决定

rds = np.random.random(6)
print(rds)

rds2 = np.random.random((3,5))
print(rds2)

# rand类似，但是传递多维数组参数时不使用元组
rd3 = np.random.rand(3,5)
print(rd3)

# randn,返回一个具有正态分布的随机数组
rdn4 = np.random.randn(3,4)
print(rdn4)

#randint,生成一个随机整数的数组
rdint5 = np.random.randint(1,10,(3,4))
print(rdint5)




# 11.ndarray属性：
#    ndim：返回数组的维度（轴数/秩）
#    shape：数组的维度，用元组表示，例如2行3列：(2，3),这个元组的长度就是ndim属性
#    size：返回数组元素总个数
#    dtype：数组的元素类型
#    itemsize：数组中每个元素的字节大小

ar = np.random.randint(1,10,(2,3,4))
print(ar.ndim)
print(ar.shape)
print(ar.size)
print(ar.dtype)
print(ar.itemsize)



# 12.通过astype可修改数据类型得到一个新数组

ar = np.array([1,2,3])
print(ar)

ar2 = ar.astype(np.str)
print(ar2)

ar3 = np.array(['67','44','6','87'])
ar4 = ar3.astype(np.float)

print(ar4)



# 13.修改数组形状
#    (1)直接通过修改shape，保持shape乘积不变
#    (2)reshape：创建一个改变形状的新数组，但是和旧数组公用一个内存空间，同步修改对应元素，相当于浅拷贝
#       当shape指定位置值为-1时，会自动计算，如(3,2)改变为(2,-1),则系统会自动计算-1为3

ar = np.random.randint(1,10,(4,5))
print(ar)

ar.shape = (2,10)
print(ar)

ar2 = ar.reshape(5,4)
print(ar2)

ar2[0][0] = 888
print(ar)
print(ar2)

'''




