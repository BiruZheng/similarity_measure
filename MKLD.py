# -*- coding: utf-8 -*-
"""
Created on Thu Dec 07 14:42:52 2017

@author: Administrator
"""

#distance
import numpy as np
from math import log


def MKLDistance(i,j,con_prob,c):
    if i == j:
        return 0
    else:
        dist = 0.0
        for k in range(c):
            dist += con_prob[i][k]*log(con_prob[i][k]/con_prob[j][k],2)
            dist += con_prob[j][k]*log(con_prob[j][k]/con_prob[i][k],2)
    return dist


def MKLDistMatrix(con_prob,c):
    n = len(con_prob)
    dist_Mat = np.zeros((n,n))
    for i in range(n):
        for j in range(i,n):
            dist_Mat[i][j] = MKLDistance(i,j,con_prob,c)
            dist_Mat[j][i] = dist_Mat[i][j]
    return dist_Mat


def MKLDist_List(con_prob_Matrix,c):
    n = con_prob_Matrix.shape[0]
    MKLD_list = []
    for i in range(n):
        dist_Mat = MKLDistMatrix(con_prob_Matrix[i],c)
        MKLD_list.append(dist_Mat)
    return MKLD_list


def dist_value(X,Y,MKLD_list):
    d = len(X)
    dist = 0.0
    for i in range(d):
        dist += MKLD_list[i][X[i],Y[i]]
    return dist




'''
con_prob = np.array([[[0.571428571,0.2,0.228571429],
[0.2,0.666666667,0.133333333],
[0.266666667,0.133333333,0.6],
[0.55,0.2,0.25]],
[[0.261538462,0.615384615,0.123076923],
[0.75,0.175,0.075],
[0.244444444,0.222222222,0.533333333]]])
d = 3
MKLD_list = MKLDist_List(con_prob,d)
print dist_value([0,1],[1,0],MKLD_list)
'''

