# -*- coding: utf-8 -*-
"""
Created on Sat May 12 14:13:18 2018

@author: wangdongqi

组合所有的数据
"""
import numpy as np
import pickle

data_pre = pickle.load(open('data_pre.pkl', 'rb'))

AllPlace = pickle.load(open('AllPlace.pkl', 'rb'))
BookClass = pickle.load(open('BookClass.pkl', 'rb')) + ['OO']
BookInfo = pickle.load(open('BookInfo.pkl', 'rb'))
CostInfo = pickle.load(open('CostInfo.pkl', 'rb'))

if len(data_pre) != len(CostInfo):
    raise RuntimeError('信息不一致')

length = len(data_pre)

Data = []
for index in range(length):
    if data_pre[index][:2] == CostInfo[index][:2]:
        Data.append(data_pre[index] + CostInfo[index][2:])
    else:
        raise RuntimeError('信息错误')
    
labels = ['term', 'stuID', 'score', 'LibDoor']
labels = labels + BookClass + AllPlace

'''
存储格式：学期，学号，排名，门禁，
'''

pickle.dump(Data, open('Data.pkl', 'wb'))
pickle.dump(labels, open('labels.pkl', 'wb'))


'''
把三个学期的成绩合在一起，不要学期，学号，成绩放在最后
'''
label_tmp1 = ['term1_' + i for i in labels[3:]] + ['term1_score']
label_tmp2 = ['term2_' + i for i in labels[3:]] + ['term2_score']
label_tmp3 = ['term3_' + i for i in labels[3:]]
train_label = label_tmp1 + label_tmp2 + label_tmp3

pickle.dump(train_label, open('train_label.pkl', 'wb'))

train_x = []
train_y = []
for index in range(int(len(Data) / 3)):
    tmp = []
    for i in range(3):
        d = Data[index * 3 + i]
        tmp = tmp + d[3:] + [d[3]]
    train_x.append(tmp[:-1])
    train_y.append(tmp[-1])

pickle.dump(train_x, open('train_x.pkl', 'wb'))
pickle.dump(train_y, open('train_y.pkl', 'wb'))