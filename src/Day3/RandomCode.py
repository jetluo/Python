#!/usr/bin/env Python
#coding:utf-8
'''
Created on 2016年4月9日

@author: Administrator
'''

import random


def randomCode():
    code = []
    
    for i in range(6):
        if i == random.randint(1,5):
            code.append(str(random.randint(1,5)));
        else:
            temp = random.randint(65,90)
            code.append(chr(temp))
    print ''.join(code)
    
def randomCode2():
    code = []
    for i in range(6):
        if i == random.randint(1,5):
            code.append(str(i));
        else:
            code.append(chr(random.randint(65,90)))
    print ''.join(code)
     
def randomCode3():
    code = []
    for i in range(6):
        code.append(str(i))  if  i == random.randint(1,5) else code.append(chr(random.randint(65,90)))
    print ''.join(code)
                
randomCode()
randomCode2()
randomCode3()

