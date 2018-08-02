# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 14:28:39 2017

@author: Administrator
"""


import numpy as np

#Smirnov返回某一属性的2个值的相似度
def Smirnov(i, j, Frequence, N):
    if i == j:
        sim = 2+float(N-Frequence[i])/Frequence[i]
        for x in Frequence:
            sim += float(x)/(N-x)
        sim -= float(Frequence[i])/(N-Frequence[i])
    else:
        sim = 0.0
        for y in Frequence:
            sim += float(y)/(N-y)
        del_ta = float(Frequence[i])/(N-Frequence[i])+float(Frequence[j])/(N-Frequence[j])
        sim -= del_ta
    return sim
    

#SmirnovMatrix返回某一属性的相似矩阵
def SmirnovMatrix(Frequence, N):
    n = len(Frequence)
    SimMatrix = np.zeros((n,n))
    for i in range(n):
        for j in range(i,n):
            SimMatrix[i][j] = Smirnov(i, j, Frequence, N)
            SimMatrix[j][i] = SimMatrix[i][j]
    return n, SimMatrix


#SmirnovMatrix_list返回存放d个相似矩阵的列表
def SmirnovMatrix_list(Freq_Matrix, N):
    d = len(Freq_Matrix)
    Smirnov_list = []
    sum_n = 0.0
    for i in range(d):
        n, SimMatrix = SmirnovMatrix(Freq_Matrix[i], N)
        sum_n += n
        Smirnov_list.append(SimMatrix)
    return sum_n, Smirnov_list

#SmirnovValue返回2条数据的相似度
def SmirnovValue(X, Y, sum_n, Smirnov_list):
    d = len(X)
    sim = 0.0
    for i in range(d):
        sim += Smirnov_list[i][X[i],Y[i]]
    return sim/sum_n


Freq_Matrix = [[35,50,15],[57,28,15],[20,55,25]]
N = 100
sum_n, Smirnov_list = SmirnovMatrix_list(Freq_Matrix, N)
X = [0,0,2]
Y = [1,0,1]
print SmirnovValue(X, Y, sum_n, Smirnov_list)