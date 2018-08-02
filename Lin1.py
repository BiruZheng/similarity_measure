# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 08:50:48 2017

@author: Administrator
"""


from math import log 
import numpy as np

#Lin1 Similarity
#Lin1Sim返回某一属性的2个值的相似度
def Lin1Sim(i, j, prob):
    p = 0
    q = 0
    min_ = min(prob[i], prob[j])
    max_ = max(prob[i], prob[j])
    for x in prob[:-1]:
        if x >= min_ and x <= max_:
            p += log(x,2)
            q += x
    return p, 2*log(q,2)

#Lin1SimMatrix返回某一属性的相似矩阵和权重矩阵
def Lin1SimMatrix(prob):
    n = len(prob) - 1
    SimMatrix = np.zeros((n,n))
    SimWeight = np.zeros((n,n))
    for i in range(n):
        SimMatrix[i][i] = Lin1Sim(i, i, prob)[0]
        SimWeight[i][i] = SimMatrix[i][i]
        for j in range(i+1, n):
            SimMatrix[i][j] = Lin1Sim(i, j, prob)[1]
            SimMatrix[j][i] = SimMatrix[i][j]
            SimWeight[i][j] = Lin1Sim(i, j, prob)[0]
            SimWeight[j][i] = SimWeight[i][j]
    return SimMatrix, SimWeight

#LinSimMatrixList返回存放d个相似矩阵的列表和权重列表
def Lin1SimMatrixList(prob_matrix):
    d = len(prob_matrix)
    Lin1Sim_List = []
    Lin1Wei_list = []
    for i in range(d):
        SimMatrix, SimWeight = Lin1SimMatrix(prob_matrix[i])
        Lin1Sim_List.append(SimMatrix)
        Lin1Wei_list.append(SimWeight)
    return Lin1Sim_List, Lin1Wei_list

#LinSimvalue返回2条数据的相似性
def Lin1Simvalue(X, Y, prob_matrix, Lin1Sim_List, Lin1Wei_list):
    d = len(X)
    weight = 0.0
    sim = 0.0
    for i in range(d):
        weight += Lin1Wei_list[i][X[i],Y[i]]
        sim += Lin1Sim_List[i][X[i],Y[i]]
    return sim/weight


prob_matrix = [[0.35,0.5,0.15,0],[0.67,0.33,0]]
Lin1Sim_List, Lin1Wei_list = Lin1SimMatrixList(prob_matrix)
X = [0,0]
Y = [1,0]
print Lin1Simvalue(X, Y, prob_matrix, Lin1Sim_List, Lin1Wei_list)