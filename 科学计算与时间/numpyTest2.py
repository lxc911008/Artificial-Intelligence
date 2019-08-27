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

# 其中numpy的广播机制可参考  https://www.cnblogs.com/jiaxin359/p/9021726.html
#（1）维度不同，后缘维度相同，往前面加1
#（2）维度相同，有轴为1

ar7 = np.random.randint(1,10,(1,5,6))
print(ar7)
ar8 = np.random.randint(2,7,(3,1,6))
print(ar8)
ar9 = ar7 + ar8
print(ar9)


#（2）数组的矩阵积
# 矩阵积 ：两个二维矩阵满足第一个矩阵的列数与第二个矩阵的行数相同，那么可以进行矩阵的乘法，即矩阵积，矩阵积不是元素级的运算。也称点积，数量积。
# 参考：https://www.jianshu.com/p/2c4b5c9b6c4d

ar1 = np.random.randint(1,5,(2,3))
print(ar1)
ar2 = np.random.randint(2,8,(3,4))
print(ar2)

ar3 = ar1.dot(ar2) #矩阵积
print(ar3)

ar4 = np.dot(ar1,ar2) # 等同ar1.dot(ar2)
print(ar4)



#（3）数组的索引与切片
#    数组的切片：在各维度上单独切片，如果某维度都保留，则直接使用:冒号，不指定起始值和终止值
#    numpy中通过切片得到的新数组，只是原来数组的一个视图，因此对新数组进行操作也会影响原数组

ar1 = np.random.randint(1,10,(3,4,5))
print(ar1)

print(ar1[1,2,2])

print(ar1[1,1,1:4])
print(ar1[1,2,1:4])

print(ar1[1,1:3,1:4])



#    花式索引：指的是利用整数数组进行索引的方式
ar1 = np.arange(30).reshape(5,6)
print(ar1)

#    获取0，3，4行的数据
print(ar1[[0,3,4]])

#    获取0，3，4行的1到3数据
print(ar1[[0,3,4],1:4])

#    ar1[[0,3,4],[1,2,3]]获取的是对应的01，32，43位置的数据,如果想达到获取0，3，4行的1到3的数据，需要使用索引器ix_函数
print(ar1[[0,3,4],[1,2,3]])
print(ar1[np.ix_([0,3,4],[1,2,3])])



#    布尔类型索引：利用布尔类型的数组进行数据索引，最终返回的结果是对应索引数据中数据为True位置的值
aw1 = np.array([1,2,3,4])
aw2 = np.array([True,False,False,True])
print(aw1[aw2])

ar1 = np.random.random((4,5))
print(ar1)

ar2 = ar1 < 0.5
print(ar2)

ar3 = ar1[ar2]
print(ar3)


#（4）数组的转置与轴对换
#    数组的转置是指将shape进行重置操作，并将其值重置为原始shape元组的倒置，比如原始的shape的值为（2，3，4），那么转置后的shape值为（4，3，2）
#    可以通过调用数组的transpose函数或者T属性进行转置操作
ar1 = np.random.randint(1,5,(3,4))

print(ar1)
ar2 = ar1.T
ar3 = ar1.transpose()

print(ar2)
print(ar3)



#  transpose(0,1,2) 其中 0，1，2为shape对应轴标志，可以修改对应顺序，转置相当于transpose(2,1,0)

ar1 = np.random.randint(1,5,(3,4,5))
print(ar1)
ar2 = ar1.transpose(2,1,0)  #相当于把shape变为 （5，4，3）
print(ar2)

ar3 = ar1.transpose(1,0,2)  #相当于把shape变为 （4，3，5）
print(ar3)



#（5）数组的拉伸与合并
#    数组的拉伸：np.tile(A,rep)函数可以将数组A进行拉伸，沿着A的维度重复rep次
ar1 = np.random.randint(1,8,(2,3))
print(ar1)

ar2 = np.tile(ar1,2) # 横向拉伸2次
print(ar2)

ar3 = np.tile(ar1,(3,4)) # 纵向拉伸3次，横向拉伸4次
print(ar3)



#    数组的合并：对于ndarry数组而言，多个数组可以执行合并操作，合并的方式有多种
#    Stack(arrays,axis=0):沿着新的轴加入一系列数组，合并的数组需要shape相同
#    vstack():堆栈数组垂直顺序（行），纵向合并
#    hstack():堆栈数组水平顺序（列），横向合并

a = np.array([[1,2,3],
             [4,5,6]])
b = np.array([[1,2,3],
             [4,5,6]])
c = np.array([[1,2,3],
             [4,5,6]])
d = np.array([[1,2,3],
             [4,5,6]])
e = np.array([1,2,3])
f = np.array([4,5,6])

print("======一个一维数组 start======")
# 一个一维数组
hh = np.stack((e,), axis=0)  #stack方法，后面的axis若不传，默认为0
print(hh)

gg = np.stack((e,), axis=1)
print(gg)

print("======一个一维数组 end======")

# axis 决定在哪一轴上添加[],例如axis = 0,就是在0轴上添加[],即添加的[]为0轴，[1,2,3]变为[[1,2,3]]
# 如果axis = 1,则添加的[]要为1轴，[1,2,3]变为[[1],[2],[3]]

print("======一个二维数组 start======")

# 一个二维数组
nn = np.stack((a,),axis=0)
print(nn)

nn2 = np.stack((a,),axis=1)
print(nn2)

nn3 = np.stack((a,),axis=2)
print(nn3)

print("======一个二维数组 end======")

print("======两个一维数组 start======")

# 两个一维数组
hk = np.stack((e,f),axis=0)
print(hk)

hk1 = np.stack((e,f),axis=1) #两个一维数组，[1,2,3]  [4,5,6]  在1轴合并，单个是[[1],[2],[3]]  [[4],[5],[6]],合起来是[[1,4],[2,5],[3,6]]
print(hk1)

print("======两个一维数组 end======")

print("======两个二维数组 start======")

bm = np.stack((a,b),axis=0)
print(bm)

print("======")

bm1 = np.stack((a,b),axis=1)
print(bm1)

print("======")

bm2 = np.stack((a,b),axis=2)
print(bm2)


print("======两个二维数组 end======")

print("======纵向合并 start======")

hb = np.vstack((a,b))
print(hb)

print("======纵向合并 end======")

print("======横向合并 start======")

kl = np.hstack((a,b))
print(kl)

print("======横向合并 end======")



#（6）通用函数：快速的元素级数组成函数
#     ufunc：numpy模块中对ndarray中数据进行快速元素级运行的函数，也可以看作是简单的函数（接收一个或多个标量值，并产生一个或多个标量值）的矢量化包装器
#     一元函数和二元函数

# abs,fabs : 计算整数，浮点数或者复数的绝对值，对于非复数，可以使用更快的fabs
n = np.array([-1,3,-5,6])
n2 = np.abs(n)
print(n2)
n3 = np.fabs(n)
print(n3)

# sqrt : 计算各个元素的平方根，要求arr每个元素为非负数
arr = np.random.randint(1,10,(2,3))
print(arr)
print(np.sqrt(arr))

# square : 计算各个元素的平方
# exp : 计算各个元素的指数e的x次方，x为各元素的值
# log,log10,log2,log1p：分别计算自然对数，底数为10的log，底数为2的log，以及log(1+x),要求arr中的每个元素为正数
# sign：计算各个元素的正负号，1 整数，0 零，-1 负数
# ceil : 计算各个元素的ceiling值，即大于等于该值的最小整数，向上取整
# floor : 计算各个元素的floor值，即小于等于该值的最大整数，向下取整
# rint : 将各个元素四舍五入到最接近的整数，保留dtype的类型
# round : 将各个元素四按照保留小数位数进行四舍五入，np.round(arr,1)



# modf : 将数组中元素的小数位和整数位以两部分独立数组形式返回,小数部分在前，整数部分在后
# isnan : 返回一个表示“那些值是NaN(不是一个数字)”的布尔类型数组，数字为false,np.NaN为true
# isfinite,isinf : 分别表示“那些元素是有穷的（非inf,非NaN）”或者“那些元素是无穷的”的布尔型数组
# cos,cosh,sin,sinh,tan,tanh：普通以及双曲型三角函数
# arccos,arccosh,arcsin,arcsinh,arctan,arctanh ：反三角函数

ji = np.array([1.23,3,4.5])
k = np.modf(ji)
print(k)



# mod : 元素级的求模运算（除法取余） np.mod(arr1,arr2)
# dot : 两个数组的点积
# greater（大于）,greater_equal,less（小于）,less_equal,equal（等于）,not_equal：执行元素级别的比较运算，最终返回一个布尔类型数组
# logical_and（两者都为真，返回真）,logical_or（两者有一个真，返回真）,logical_xor（两者不同返回真） : 执行元素级别的布尔逻辑运算，相当于缀运算符&，|，^
# power : 求解对数组中的每个元素进行给定次数的指数值，类似于 arr ** 3



#（7）聚合函数
#     聚合函数是对一组值进行操作，返回一个单一值，作为结果的函数。当然聚合函数也可以指定对某个具体的轴进行数据聚合操作，通过axis = 轴数进行指定
#     常见的聚合操作有：平均值，最大值，最小值，总体标准偏差等等
arr = np.random.randint(1,10,(2))
print(arr)
print(np.sum(arr)) #求和
print(np.max(arr)) #最大
print(np.min(arr)) #最小
print(np.mean(arr)) #平均值
print(arr - np.mean(arr)) # 偏差
print(np.mean((arr - np.mean(arr)) ** 2)) # 方差  偏差的平方的平均值
print(np.std(arr)) #标准差  方差的平方根



#（8）np.where函数
#    是三元表达式x if condition else y的矢量化版本
arr1 = np.array([1,3,5,6,2])
arr2 = np.array([7,9,3,5,4])

cond = arr1 < arr2
print(cond)

result = [x if z else y for x,y,z in zip(arr1,arr2,cond)]
print(result)

re2 = np.where([True,False],[1,3],[2,6]) # 取对应true位置的值
print(re2)

re3 = np.where([[True,False],[True,True]],[[1,3],[4,6]],[[5,7],[2,8]])
print(re3)

re4 = np.where(cond,arr1,arr2)
print(re4)



#（9）np.unique函数
#    将数组中的元素进行去重操作
n1 = np.random.randint(1,10,(4,5))
print(n1)
print(np.unique(n1))

'''


