#!/usr/bin/env Python
#coding:utf-8
'''
Created on 2016年4月9日

@author: Administrator
'''
from inspect import ArgInfo
'''
多个函数传递
'''
def printinfo(name,age = 50):
    print "Name:",name;
    print "Age:",age;
    return;

'''
缺省函数，可传可不传输
'''
def printinfo1(name,age = 50):
    print "Name:",name;
    print "Age:",age;
    return;
'''
可变函数
'''
def printinfo2(name,*var):
    print "Name:",name;
    print sum(1,2)
    for age in var:
        print "Age:",age;
    return;
'''
匿名函数
'''
sum = lambda arg1,arg2:arg1 + arg2;

'''
传递字典
'''
def show(**args):
    print args['value']
    return args;

#yield

def foo1():
    yield 1
    yield 2
    yield 4
    yield 8
    

def AlexReadlines():
    seek = 0
    while True:
        with open('D:/09_cissp/A.txt','r') as f:
            f.seek(seek)
            data = f.readline()
            if data:
                seek = f.tell()
                yield data
            else:
                return

