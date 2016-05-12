#!/usr/bin/env Python
#coding:utf-8
'''
Created on 2016年4月9日

@author: Administrator
'''
from Day3 import Function1
import Function2;
from _random import Random

Function2.printinfo("MAOMAO", 18);
Function2.printinfo1("MINGMING");
Function2.printinfo2("xiaolei",32,34);

name = Function2.sum(10,23)
print "调用sum的结果：", name

user_dict = {'name':'Liyang','value':'zhangbign'};
args = Function2.show(**user_dict)

print range(20)
print xrange(20)
#for item in xrange(10):
#    print item
    
re = Function2.foo1()
print re
for i in re:
    print i
    

for item in Function2.AlexReadlines():
    print item


print 'gt' if 1  > 3 else 'lt';

a = []
print dir(a)
print vars()


li = ['汽车','大炮','美女']
for it in enumerate(li,12323):
    print it[0],it[1]
    
a = '8*8'
print eval(a) 


Founction1 = __import__('Function1')
#Founction1.Bar()
bar = getattr(Founction1, 'Bar')
print bar()
import random
print random.random();
print random.randint(1,3);
print random.randrange(1,5);
print chr(random.randint(65,90));
#import os
#print __import__('sys').path

