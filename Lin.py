# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 19:56:05 2017

@author: Administrator
"""

from math import log 
import numpy as np


#Lin Similarity
#LinSim返回某一属性的2个值的相似度
def LinSim(i, j, prob):
    #prob为第k个属性各个值的概率，prob[-1] == 1表示该属性为有序的
    if i == j:
        sim = 2*log(prob[i], 2)
    elif prob[-1] == 1:
        #odernal Values
        sim = 2 * log(sum(prob[i:j+1] if i < j else prob[j:i+1]), 2)
    else:
        sim = 2 * log(prob[i] + prob[j], 2)
    return sim

#LinSimMatrix返回某一属性的相似矩阵
def LinSimMatrix(prob):
    n = len(prob) - 1
    SimMatrix = np.zeros((n,n))
    for i in range(n):
        for j in range(i,n):
            SimMatrix[i][j] = LinSim(i, j, prob)
            SimMatrix[j][i] = SimMatrix[i][j]
    return SimMatrix

#LinSimMatrixList返回存放d个相似矩阵的列表
def LinSimMatrixList(prob_matrix):
    d = len(prob_matrix)
    Lin_List = []
    for i in range(d):
        SimMatrix = LinSimMatrix(prob_matrix[i])
        Lin_List.append(SimMatrix)
    return Lin_List


#TransProb返回数据X各个属性值所对应的概率值
def TransProb(X,prob_matrix):
    d = len(X)
    X_ = [0] * d
    for i in range(d):
        X_[i] = prob_matrix[i][X[i]]
    return X_


#LinSimvalue返回2条数据的相似性
def LinSimvalue(X, Y, prob_matrix, Lin_List):
    d = len(X)
    X_ = TransProb(X, prob_matrix)
    Y_ = TransProb(Y, prob_matrix)
    weight = 0.0
    sim = 0
    for i in range(d):
        weight += log(X_[i] * Y_[i],2)
        sim += Lin_List[i][X[i],Y[i]]
    return sim/weight


prob_matrix = [[0.35,0.54,0.11,0]]
Lin_List = LinSimMatrixList(prob_matrix)
X = [2]
Y = [2]
print LinSimvalue(X, Y, prob_matrix, Lin_List)




