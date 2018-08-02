# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 10:20:49 2017

@author: Administrator
"""


def Eskin(X, Y, Attribute):
    d = len(X)
    sim = 0
    for i in range(d):
        if X[i] == Y[i]:
            sim += 1
        else:
            sim += pow(Attribute[i],2)/(2.0 + pow(Attribute[i],2))
    return sim/d

Attribute = [3,5,6,4,6,3]
X = [1,3,2,2,1,2]
Y = [2,4,2,2,5,2]
print Eskin(X, Y, Attribute)

'''==================================================================='''


def Overlap(X, Y):
    d = len(X)
    sim = 0.0
    for i in range(d):
        if X[i] == Y[i]:
            sim += 1
    return sim/d

X = [1,2,3,4,3,2,1]
Y = [2,2,3,1,4,3,1]
print Overlap(X,Y)
