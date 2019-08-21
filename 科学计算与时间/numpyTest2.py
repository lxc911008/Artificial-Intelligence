#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:LXC
@file: numpyTest2.py
@time: 2019/08/21
"""

import numpy as np

'''
numpy基本操作
（1）数组与标量、数组之间的运算
（2）数组的矩阵积
（3）数组的索引与切片
（4）数组的转置与轴对换
（5）数组的拉伸与合并
（6）通用函数：快速的元素级数组成函数
（7）聚合函数
（8）np.where函数
（9）np.unique函数

'''

'''


'''
# （1）数组与标量、数组之间的运算
# 矢量化数组运算，传统需要通过for循环运算
#数组与标量矢量化运算
ar = np.array([1,2,3,4])
ar += 10
print(ar)

#数组与数组之间的运算
ar2 = np.random.randint(1,10,(3,5))
print(ar2)
ar3 = np.random.randint(2,7,(3,5))
print(ar3)
ar4 = ar2 * ar3
print(ar4)

