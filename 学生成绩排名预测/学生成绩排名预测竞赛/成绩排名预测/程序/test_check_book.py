# -*- coding: utf-8 -*-
"""
Created on Mon May  7 14:53:24 2018

@author: wangdongqi

读取书籍信息，检查数据中可能出现的问题
"""

Book = dict()
ClassNum = []
err = []

with open('图书类别.txt', encoding = 'utf-8') as f:
    f.readline();
    for line in f:
        (BookNumber, BookClass) = line.split('\t');
        if BookNumber not in Book.keys():
            Book[BookNumber] = [BookClass]
        else:
            Book[BookNumber].append(BookClass)
            print(BookNumber)
            err.append(BookNumber)
        if BookClass not in ClassNum:
            ClassNum.append(BookClass);

# 测试重复的那些数据是否有变化
err_list = []
for i in err:
    tmp_list = Book[i]
    tmp = tmp_list[0]
    for j in tmp_list[1:]:
        if j != tmp:
            err_list.append(i)
            break
# 结论：所有重复的数据的信息相同，对结果无影响



