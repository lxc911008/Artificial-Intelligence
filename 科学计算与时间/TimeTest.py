#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:LXC
@file: TimeTest.py
@time: 2019/08/18
"""

import time

# 时间方法调用说明

'''
# 返回格林威治西部的夏令时地区偏移秒数
alz = time.altzone
print(alz)


# 接收时间元组，返回一个可读形式（“Tue Dec 11 18:07:14 2008”）24个字符的字符串,不传参数默认当前时间
asTim = time.asctime((2018,8,15,23,34,56,4,5,6))
print(asTim)


# linux  返回进程时间   
# windows  第一次调用返回进程时间，第二三次调用返回第一次调用到现在的运行时间
clo = time.clock()

for i in range(100000000):
    pass

clo2 = time.clock()

print(clo2)

for i in range(100000000):
    pass

clo3 = time.clock()

print(clo3)



# 作用相当于astime,参数传递秒数
time.ctime()


# 接收时间戳（1970纪元后经过的浮点秒数），并返回当地时间元组
loc = time.localtime()
print(loc)

act = time.asctime(loc)
print(act)



# 接收时间元组，返回时间戳
mkt = time.mktime(time.localtime())
print(mkt)



# 推迟线程的运行
time.sleep(4)
print('运行结束')



# 接收时间元组，返回指定格式的字符串，由fmt决定
srf = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
print(srf)



# 把时间字符串转化为时间元组
stp = time.strptime("2018-09-15 15:34:42","%Y-%m-%d %H:%M:%S")
print(stp)



# 返回当前时间的时间戳
tm = time.time()
print(tm)

ct = time.ctime(tm)
print(ct)

'''


