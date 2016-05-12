#!/usr/bin/env Python
#coding:utf-8
'''
Created on 2016年4月9日

@author: Administrator
'''
import pickle
#实现进程间内容的共享
li = ['alex',12,23,'ok','maomao']
print pickle.dumps(li)
print pickle.loads(pickle.dumps(li))
print type(pickle.dumps(li))
#dump序列号到文件中去
pickle.dump(li, open('D:/pick.txt','wb'))
#load反序列化文件
print pickle.load(open('D:/pick.txt','r'))

import json

name_dict = {'name':'maomao','age':23}
print json.dumps(name_dict)
print json.loads(json.dumps(name_dict))


import re

result1  = re.match('\d+', 'asdfja;lsdf2323kjasdfl;ksadf')
result2 = re.search('\d+', 'asdfja;lsdf2323kjasdfl;ksadf')
print type(re.compile('\d+'))
print result1 #.group()
print result2.group()

com = re.compile('\d+','2asdfas2dfasdf')
com.findall()
