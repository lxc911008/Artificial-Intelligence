#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:LXC
@file: pandasTest1.py
@time: 2019/08/27
"""

import pandas as pd

'''
pandas中主要有两种数据结构，分别是Series和DataFrame

Series:一种类似于一维数组的对象，是由一组数据（各种Numpy类型）以及一组与之相关的数据标签（即索引）组成。
       仅由一组数据也可产生简单的Series对象，注意：Series中的索引值是可以重复的。

DataFrame:一个表格型的数据结构，包含一组有序的列，每列可以是不同的值类型（数值、字符串、布尔型等），
          DataFrame即有行索引也有列索引，可以看作是由Series组成的字典

'''

