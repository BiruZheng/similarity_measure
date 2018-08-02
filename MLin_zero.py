# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 19:34:51 2017

@author: Administrator
"""

from math import log
import numpy as np


def MLinSim(i, j, Cond_Prob):
    if i == j:
        sim = 2*sum([log(p,2) for p in Cond_Prob[i] if p > 0])
    else:
        sim = 2*sum([log(p,2) for p in Cond_Prob[i]+Cond_Prob[j] if p > 0])
    return sim


def MLinSimMatrix(Cond_Prob):
    n = len(Cond_Prob)
    SimMatrix = np.zeros((n,n))
    for i in range(n):
        for j in range(i,n):
            SimMatrix[i][j] = MLinSim(i, j, Cond_Prob)
            SimMatrix[j][i] = SimMatrix[i][j]
    return SimMatrix


def MLinSimMatrixList(Cond_prob_matrix):
    d = len(Cond_prob_matrix)
    MLin_List = []
    for i in range(d):
        SimMatrix = MLinSimMatrix(Cond_prob_matrix[i])
        MLin_List.append(SimMatrix)
    return MLin_List


def TransProb(X,Cond_prob_matrix):
    d = len(X)
    X_ = [0] * d
    for i in range(d):
        X_[i] = Cond_prob_matrix[i][X[i]]
    return np.array(X_)


def MLinSimvalue(X, Y, Cond_prob_matrix, MLin_List, C):
    d = len(X)
    X_ = TransProb(X, Cond_prob_matrix)
    Y_ = TransProb(Y, Cond_prob_matrix)
    weight = 0.0
    sim = 0
    info = X_*Y_
    for i in range(d):
        sim += MLin_List[i][X[i],Y[i]]
        #weight += sum([log(p,2) for p in X_[i] if p > 0])
        #weight += sum([log(q,2) for q in Y_[i] if q > 0])
        weight += sum([log(p,2) for p in info[i] if p > 0])
    return sim/weight


'''
Cond_Prob1 = [[20.0/35,0.0,15.0/35],[12.0/60,40.0/60,8.0/60],[6.0/15,0.0,9.0/15],[22.0/40,8.0/40,10.0/40]]
Cond_Prob2 = [[17.0/65,40.0/65,8.0/65],[3.0/4,1.0/4,0.0],[11.0/45,10.0/45,24.0/45]]
Cond_Prob3 = [[17.0/25,6.0/25,2.0/25],[27.0/55,15.0/55,13.0/55],[8.0/40,20.0/40,12.0/40],[0.0,16.0/30,14.0/30]]
Cond_prob_matrix = [Cond_Prob1, Cond_Prob2, Cond_Prob3]

MLin_List = MLinSimMatrixList(Cond_prob_matrix)
X = [0,1,0]
Y = [1,0,2]
print MLinSimvalue(X, Y, Cond_prob_matrix, MLin_List, 3)


A = [[20.0/58,7.0/57,8.0/35],[12.0/58,40.0/57,8.0/35],[4.0/58,2.0/57,9.0/35],[22.0/58,8.0/57,10.0/35]]
B = [[17.0/58,40.0/57,8.0/35],[30.0/58,7.0/57,3.0/35],[11.0/58,10.0/57,24.0/35]]
C = [[17.0/58,6.0/57,2.0/35],[27.0/58,15.0/57,13.0/35],[8.0/58,20.0/57,12.0/35],[6.0/58,16.0/57,8.0/35]]
D = [A,B,C]
E = MLinSimMatrixList(D)
print MLinSimvalue(X, Y, D, E, 3)
'''
