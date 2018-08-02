# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 10:09:18 2017

@author: Administrator
"""

import numpy as np
from math import log



def MLinSim(i, j, Cond_Prob, C):
    w = 0.0
    for k in range(C):
        w += log(Cond_Prob[i][k]*Cond_Prob[j][k],2)
    if i == j:
        sim = 2*sum([log(p,2) for p in Cond_Prob[i]])
    elif Cond_Prob[-1] == 1:
        p = np.sum(Cond_Prob[i:j+1] if i<j else Cond_Prob[j:i+1], axis = 0)
        sim = 2 * sum([log(x,2) for x in p])
    else:
        C_list = map(lambda p,q: log(p+q,2),Cond_Prob[i],Cond_Prob[j])
        sim = 2*sum(C_list)
    return sim/w

'''
def weight(i, j, Cond_Prob, C):
    w = 0.0
    for k in range(C):
        w += log(Cond_Prob[i][k]*Cond_Prob[j][k])
    return w
'''


C = [[17.0/58,6.0/57,2.0/35],[27.0/58,15.0/57,13.0/35],[8.0/58,20.0/57,12.0/35],[6.0/58,16.0/57,8.0/35],1]
D = [[17.0/25,6.0/25,2.0/25],[27.0/55,15.0/55,13.0/55],[8.0/40,20.0/40,12.0/40],[6.0/30,16.0/30,8.0/30],1]
for i in range(4):
    for j in range(i,4):
        print MLinSim(i, j, C, 3),' ',MLinSim(i, j, D, 3)


'''
def MLinSim(i, j, Cond_Prob, C):
    n = len(Cond_Prob)
    w = float(n)/C
    if i == j:
        sim = 2*sum([log(p,2) for p in Cond_Prob[i]])
    elif Cond_Prob[-1] == 1:
        pass
    else:
        C_list = map(lambda p,q: log(p+q,2),Cond_Prob[i],Cond_Prob[j])
        sim = 2*w*sum(C_list)
    return sim
'''