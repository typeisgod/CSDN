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
#file_type=open('图书类别.txt','r')

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

'''
新增 月平均 月方差 月最大 月最小 
     日平均  日方差 日最大 日最小
    06-22 小时点次数
    共 25 维
0    1    2    3    4567 891011      12-28 29-71
学期 学号 排名  总数 月   日          06-22  1-43
'''
line = file_library.readline()
line = file_library.readline()#直接读取第二行数据 
zero26=np.zeros(26,int).tolist();
i=0
while i<len(data):
    data[i]=data[i]+zero26;
    i=i+1

data3=np.zeros(shape=(len(data),6,31)).tolist();#统计每天的次数 每个月取31天 
'''1/3学期 data3[index][0-4]表示 9-1月 9~0 10~1 11~2 12~3 1~4
     2学期 data3[index][0-5]表示 2-7月
'''
n_1=5;#1 3 学期 5个月
n_2=6;# 2 学期 6个月
while line:
    readtime=0#记录读取次数 第一次读学期 第二次为学号
    (seme,sid,date,time,ent)=line.split('\t')
    seme=int(seme);
    sid=int(sid);
    index=(sid-1)*3+seme-1;#第seme的第sid号学生在data中的下标号  
    data[index][3]+=1;#学期签到总数
    offset=6;#小时签到次数对应data列的偏移量
    #统计小时签到次数
    hour=int(time[0:2]);
    data[index][hour+offset]+=1;
    month=int(date[0:2]);

    day=int(date[2:])
    if seme!=2:
        data3[index][(month-9)%12][day-1]+=1;
    else:
        data3[index][month-2][day-1]+=1;
    line = file_library.readline()
    
'''
根据data2和data3求均值 最大 最小 方差 并写入到data里
'''    
i=0
while i<len(data):
    if i%3==1:#是否为第二学期
        n=n_2;
    else:
        n=n_1;
    mmean=data[i][3]/n;
    dmean=data[i][3]/(n*31);
    m=np.zeros(n,int).tolist();#该人每个人的总数
    d=np.zeros(n*31,int).tolist()#该人每天的总数
    j=0#第j个月
    l=0#该学期第l天
    while j<n:
        m[j]=int(sum(data3[i][j]))
        k=0#第j月中的k天
        while k<31:
            d[l]=int(data3[i][j][k])
            l=l+1
            k=k+1
        j=j+1
    mmax=max(m);
    dmax=max(d);
    mmin=min(m);
    dmin=min(d);
    mvar=np.var(m);
    dvar=np.var(d);
    data[i][4:12]=mmean,mvar,mmax,mmin,dmean,dvar,dmax,dmin;
    i=i+1
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
'''
新增内容：
72 74 74 75     76 77 78 79
月总借书        日总借书
均值 方差 最大 最小
☞统计各种类书之和
'''
data2=np.zeros(shape=(len(data),6,31)).tolist();#统计每个学期每个人 某月的第某天借了几本书

BookInfo=pickle.load(open('BookInfo.pkl','rb'))
zero43=np.zeros(43,int).tolist()
i=0
offset=30 #书类别偏移
while i<len(data):
    data[i]+=zero43
    i=i+1
line=file_borrow.readline()
line=file_borrow.readline()

while line:
    (seme,sid,name,date,ent)=line.split('\t')
    index=(int(sid)-1)*3+int(seme)-1
    month=int(date[:2])
    day=int(date[2:])
    if int(seme)!=2:
        data2[index][(month-9)%12][day-1]+=1;
    else:
        data2[index][month-2][day-1]+=1;
    if name not in BookInfo.keys():
        data[index][42+offset-1]+=1
    else:
        i=0
        while i<len(BookClass)-1:
            if BookClass[i]==BookInfo[name]:
                break;
            i=i+1
        data[index][i+offset-1]+=1
    line=file_borrow.readline()
i=0
'''
计算月 日 放进 data
'''
zeros8=np.zeros(8,int).tolist();
while i<len(data):
    data[i]+=zeros8
    i=i+1
i=0
while i<len(data):
    if i%3==1:
        n=n_2
    else:
        n=n_1
    num=sum(data[i][offset-1:])#某个人某学期总借书量
    mmean=num/n;
    dmean=num/(n*31);
    m=np.zeros(n,int).tolist();
    d=np.zeros(n*31,int).tolist();
    j=0#第j个月
    l=0#该学期第l天
    while j<n:
        m[j]=int(sum(data2[i][j]))
        k=0#第j月中的k天
        while k<31:
            d[l]=int(data2[i][j][k])
            l=l+1
            k=k+1
        j=j+1
    mmax=max(m);
    dmax=max(d);
    mmin=min(m);
    dmin=min(d);
    mvar=np.var(m);
    dvar=np.var(d);
    data[i][72:]=mmean,mvar,mmax,mmin,dmean,dvar,dmax,dmin;
    i=i+1
    
    
''' 学期、学号、排名、门禁、书籍信息 '''
#pickle.dump(data, open('data_pre.pkl', 'wb'))
