# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 16:21:38 2017

@author: Administrator
"""

import numpy as np
from math import log 

def Burnaby(i, j, prob):
    if i == j:
        sim = 1
    else:
        son = 0.0
        for x in prob:
            son += 2*log(1-x,2)
        mom = log(prob[i]*prob[j]/((1-prob[i])*(1-prob[j])),2)+son
        sim = son/mom
    return sim


def BurnabyMatrix(prob):
    n = len(prob)
    SimMatrix = np.zeros((n,n))
    for i in range(n):
        for j in range(i,n):
            SimMatrix[i][j] = Burnaby(i, j, prob)
            SimMatrix[j][i] = SimMatrix[i][j]
    return SimMatrix


def BurnabyMatrixList(prob_matrix):
    d = len(prob_matrix)
    Burnaby_List = []
    for i in range(d):
        SimMatrix = BurnabyMatrix(prob_matrix[i])
        Burnaby_List.append(SimMatrix)
    return Burnaby_List


def SimValue(X, Y, Burnaby_List):
    d = len(X)
    Burnaby_sim = 0.0
    for i in range(d):
        Burnaby_sim += Burnaby_List[i][X[i],Y[i]]
    return Burnaby_sim/d

prob_matrix = [[0.35,0.54,0.11],[0.57,0.28,0.15]]
Burnaby_List = BurnabyMatrixList(prob_matrix)

