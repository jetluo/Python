#!/usr/bin/env Python
#coding:utf-8
'''
Created on 2016年4月9日

@author: Administrator
'''
import hashlib

hash = hashlib.md5()
hash.update('admin')
print hash.hexdigest()
print hash.digest()