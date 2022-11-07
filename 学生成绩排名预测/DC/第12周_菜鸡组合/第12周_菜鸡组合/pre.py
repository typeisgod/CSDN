# -*- coding: utf-8 -*-
"""
Created on Mon May  7 13:28:12 2018

@author: Type真是太帅了
"""
import numpy as np
import pickle
file_rank=open('成绩.txt','r')
file_library=open('图书馆门禁.txt','r')
file_borrow=open('借书.txt','r')
file_consume=open('消费.txt','r')
file_type=open('图书类别.txt','r')

'''
 学期 学号 图书馆门禁次数 食堂总消费 交通总消费 宿舍总消费 超市总消费 书类别  排名
'''  
data=[]
'''
读入成绩
'''
line = file_rank.readline()
line = file_rank.readline()#直接读取第二行数据 
while line:  
    temp=[]
    pre=0
    while pre<len(line)-2: #对于每行line的每个字符 将其转化为数字形式并存储于数组中 最后\n两个字符不读
        if line[pre]!='\t':
            end=pre+1
            while end<len(line)-1:
                if line[end]=='\t':
                    temp=temp+[int(line[pre:end])]
                    pre=end+1
                    break
                else:
                    end=end+1
        else:
            pre=pre+1
            end=pre+1
    data=data+[temp]
    line = file_rank.readline()  
'''
以学号为主key 学期为负key进行排序
'''
data=sorted(data,key=lambda x:(x[1],x[0]))

'''
读入图书馆门禁次数(学期计)
'''
line = file_library.readline()
line = file_library.readline()#直接读取第二行数据 
i=0
while i<len(data):
    data[i]=data[i]+[0]
    i=i+1
while line:
    readtime=0#记录读取次数 第一次读学期 第二次为学号
    xueqi=int(line[0:1])
    xuehao=2
    end=2
    while end<len(line)-2:
        if line[end]=='\t':
            xuehao=int(line[2:end])
            break
        end+=1
    index=(xuehao-1)*3+xueqi-1
    data[index][3]+=1
    line = file_library.readline()  
'''
借书
'''
"""
读取书籍信息
"""

BookInfo = dict()
BookClass = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','TB','TD','TE','TF','TG','TH','TJ','TK','TL','TM','TN','TP','TQ','TS','TT','TU','TV','U','V','X','Y', 'Z','OO']
'''
pickle.dump(BookInfo,open('BookInfo.pkl','wb'))
'''
'''
with open('图书类别.txt', encoding = 'utf-8') as f:
    f.readline();
    for line in f:
        line = line.replace('\n', '')
        (BookNumber, bookclass) = line.split('\t');
        if not BookNumber.isdigit():
            continue
        
        BookInfo[BookNumber] = bookclass
'''
BookInfo=pickle.load(open('BookInfo.pkl','rb'))
zero43=np.zeros(43,int).tolist()
i=0
offset=4
while i<len(data):
    data[i]+=zero43
    i=i+1
line=file_borrow.readline()
line=file_borrow.readline()

while line:
    (seme,sid,name,date,ent)=line.split('\t')
    index=(int(sid)-1)*3+int(seme)-1
    if name not in BookInfo.keys():
        data[index][43+offset-1]+=1
    else:
        i=0
        while i<len(BookClass)-1:
            if BookClass[i]==BookInfo[name]:
                break;
            i=i+1
        data[index][i++offset-1]+=1
    line=file_borrow.readline()

''' 学期、学号、排名、门禁、书籍信息 '''
pickle.dump(data, open('data_pre.pkl', 'wb'))
