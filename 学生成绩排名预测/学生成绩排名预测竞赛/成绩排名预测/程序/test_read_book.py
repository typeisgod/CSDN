# -*- coding: utf-8 -*-
"""
Created on Mon May  7 15:49:55 2018

@author: wangdongqi

读取书籍信息
"""
BookInfo = dict()
errInfo = dict()
BookClass = []

with open('图书类别.txt', encoding = 'utf-8') as f:
    f.readline();
    for line in f:
        line = line.replace('\n', '')
        (BookNumber, bookclass) = line.split('\t');
        if not BookNumber.isdigit():
            errInfo[BookNumber] = bookclass
            continue
        
        BookInfo[BookNumber] = bookclass
        if bookclass not in BookClass:
            BookClass.append(bookclass)
        

# 排序
BookClass.sort()

# 打印42类书的类名
for i in BookClass:
    print(i, end = ' ')
    


# 保存信息
import pickle

# 保存
pickle.dump(BookInfo, open('BookInfo.pkl', 'wb'))
pickle.dump(BookClass, open('BookClass.pkl', 'wb'))

# 读取
BookInfo = pickle.load(open('BookInfo.pkl', 'rb'))
BookClass = pickle.load(open('BookClass.pkl', 'rb'))






