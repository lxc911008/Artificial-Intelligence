#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:LXC
@file: pandasTest3.py
@time: 2019/09/05
"""

import pandas as pd
import numpy as np

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



#（2）索引、选取和数据过滤:通过DataFrame的相关方式可以获取对应的列或者数据形成一个新的DataFrame,方便后续进行统计计算
#     对于DataFrame/Series中的NaN一般采取的方式为删除对应列行或填充一个默认值
#     dropna:根据标签值中是否存在缺失数据对轴标签进行过滤（删除），可以通过阈值的调节对缺失值的容忍度
#     fillna:用指定值或者插值的方式填充缺失数据，比如：ffill或者bfill
#     isnull:返回一个含有布尔值的对象，这些布尔值表示那些值是缺失值
#     notnull:isnull的否定式

pf = pd.DataFrame(np.random.randint(1,10,(3,4)),index = list('abc'),columns = list('ABCD'))
print(pf)

pf.loc[['a','b'],'C'] = np.NaN

print(pf)

print(pf.isnull())
print(pf.notnull())

#dropna:根据标签值中是否存在缺失数据对轴标签进行过滤（删除），可以通过阈值的调节对缺失值的容忍度
print(pf.dropna())  #删除包含有NaN的行

print(pf.dropna(axis=1))  #删除包含有NaN的列，通过axis指定为1轴，即列，默认为0轴，即行

print(pf.dropna(how="all"))  #how="all"要求必须整行或者整列都是NaN才进行删除

#fillna:用指定值或者插值的方式填充缺失数据，比如：ffill或者bfill
print(pf.fillna("io"))  #用指定值替换NaN数据

#pf.loc['a','C'] = 6
print(pf.fillna(method = "ffill"))  #向前填充

print(pf.fillna(method = "bfill"))  #向后填充

pf.loc['a','A'] = np.NaN
print(pf.fillna({'C':'100','A':'200'})) #把C列的nan填充为100，把A列的nan填充为200

print(pf.replace({np.NaN:'hh',5:'haha'}))  #replace方法，传递一个字典，把nan替换为hh，把5替换为haha



#（3）常用的数学统计方法
# count:计算非NaN值的数量，可通过axis指定计算行或者列，默认为列
# describe:针对Series和DataFrame列计算总统计值
# min/max:计算最大值、最小值
# idxmin/idxmax:计算能够获取最大值、最小值的索引位置（整数）
# quantile:计算样本的分位数（中位数）
# sum:值的总值
# mean,median:平均数，中位数
# mad:根据平均值计算平均绝对距离差
# var:样本数值的方差
# std:样本数值的标准偏差

#关于下面的累计，都是从下往上依次计算得到新的DataFrame，默认都是列计算，可通过axis=1指定为行
# cumsum:样本值的累计和:从下往上依次累计得到新的DataFrame
# cummin、cummax:样本的累计最小值、最大值、最小值
# cumprod:样本值的累计积

# pct_change:计算百分数变化：从上往下计算增加的百分比，，默认为列计算，可通过axis=1指定为行

pf = pd.DataFrame(np.random.randint(1,10,(3,4)))
print(pf)

print(pf.describe())  # describe:针对Series和DataFrame列计算总统计值
print(pf.count(axis = 1))  # count:计算非NaN值的数量，可通过axis指定计算行或者列，默认为列（0），修改为1即统计行
print(pf.min(axis = 1))  #默认计算每一列的最小值，修改axis = 1可以计算每行

print(pf.idxmin(axis = 1))  #默认计算每列的最小值索引位置，修改axis = 1可以计算每行
print(pf.quantile(axis= 1))  #默认计算每列的中位数，修改axis = 1可以计算每行



#（4）相关系数与协方差
#    相关系数（Correlation coefficient）：反应两个样本/变量之间的相互关系以及之间的相关程度。在COV的基础上进行了无量纲化操作，也就是进行了标准化操作
#    协方差（Covariance,COV）:反映两个样本/变量之间的相互关系以及之间的相关程度。
#                            如果有X，Y两个变量，每个时刻的“X值与其均值之差” 乘以 “Y值与其均值之差” 得到一个乘积，再对这每时刻的乘积求和并求出均值
#                            如果协方差为正，说明X,Y同向变化，协方差越大说明同向程度越高，如果协方差为负，说明X,Y反向变化，协方差越小说明反向程度越高

#    相关系数：用X,Y的协方差除以X的标准差和Y的标准差，剔除了两个标量的量纲影响，标准化后的特殊协方差，在-1到+1之间变化
#             当相关系数为1时两者正向相关程度最大，同向正相关
#             当相关系数为0时，两者无关
#             当相关系数为-1时两者反向相关程度最大，同反向相关

pf = pd.DataFrame({"考试成绩":[100,90,80,70],
                   "玩游戏时间":[5,20,4,15]})

print(pf.cov())
print(pf["考试成绩"].cov(pf["玩游戏时间"]))  #协方差

print(pf.corr())
print(pf["考试成绩"].corr(pf["玩游戏时间"]))  #相关系数



#（5）唯一值，值计数以及成员资格
#     unique方法用于获取Series中的唯一值数组（去重数据后的数组）
#     value_counts方法返回一个包含值和该值出现次数的Series对象，次序按照出现的频率由高到低排序
#     isin方法用于判断矢量化集合的成员资格，可用于选取Series中或者DataFrame中列中数据的子集

pf = pd.DataFrame(np.random.randint(1,10,(3,4)),index = list("abc"),columns = list("ABCD"))
print(pf)

print(pf["A"].unique())  #去重
print(pf["B"].value_counts())  #计数

ii = pf["C"].isin([2,3])  #判断是否包含2，3
print(ii)

print(pf["C"][ii])

'''

#（6）层次索引
#     在某一个方向拥有多个（两个及两个以上）索引级别
#     通过层次化索引,pandas能够以较低维度形式处理高维度的数据
#     通过层次索引，可以按照层次统计数据
#     层次索引包括Series层次所以和DataFrame层次索引

ser = pd.Series([10,20,30,40],index = [['2017','2018','2019','2020'],['苹果','雪梨','桃子','杨桃']])
print(ser)
print(ser.index)
print(ser["2017","苹果"])

#交换分层索引
print(ser.swaplevel())
#ser2 = pd.Series([10,20,30,40],index = [['2017','2018','2019','2020'],['苹果','雪梨','桃子','杨桃'],["11","22","33","44"]])
#print(ser2)

#ser3 = ser2.swaplevel()
#print(ser3)

#转换为DataFrame索引
print(ser.unstack(level = 0))  #level 控制哪一层变为列，默认为1，stack()方法由DataFrame转变为Series

#DataFrame索引   pandas04  24:30



