# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 10:31:29 2017

@author: Administrator
"""


from math import log 
import numpy as np

#IOFSim返回同一属性2个值的相似度
#Frequence为某一属性的各个取值出现的频数
def IOFSim(i, j, Frequence):
    if i == j:
        sim = 1
    else:
        sim = 1.0/(1+log(Frequence[i],2)*log(Frequence[j],2))
    return sim

'''========================================================================='''
#OFSim返回同一属性2个值的相似度
#N表示训练集的大小
def OFSim(i, j, Frequence, N):
    if i == j:
        sim = 1
    else:
        sim = 1.0/(1+log(float(N)/Frequence[i],2)*log(float(N)/Frequence[i],2))
    return sim

#SimMatrix返回某一属性的相似矩阵
#IOFMatrix为IOF的相似矩阵；OFMatrix为OF的相似矩阵
def SimMatrix(Frequence, N):
    n = len(Frequence)
    IOFMatrix = np.zeros((n,n))
    OFMatrix = np.zeros((n,n))
    for i in range(n):
        for j in range(i, n):
            IOFMatrix[i][j] = IOFSim(i, j, Frequence)
            IOFMatrix[j][i] = IOFMatrix[i][j]
            OFMatrix[i][j] = OFSim(i, j, Frequence, N)
            OFMatrix[j][i] = OFMatrix[i][j]
    return IOFMatrix, OFMatrix

#SimMatrixList 返回存放d个相似矩阵的列表
def SimMatrixList(Freq_Matrix, N):
    d = len(Freq_Matrix)
    IOF_list = []
    OF_list = []
    for i in range(d):
        IOFMatrix, OFMatrix = SimMatrix(Freq_Matrix[i], N)
        IOF_list.append(IOFMatrix)
        OF_list.append(OFMatrix)
    return IOF_list, OF_list

#SimValue返回2条数据的相似度
def SimValue(X, Y, IOF_list, OF_list):
    d = len(X)
    IOF_sim = 0.0
    OF_sim = 0.0
    for i in range(d):
        IOF_sim += IOF_list[i][X[i],Y[i]]
        OF_sim += OF_list[i][X[i],Y[i]]
    return IOF_sim/d, OF_sim/d


Freq_Matrix = [[35,50,15],[57,28,15]]
N = 100
IOF_list, OF_list = SimMatrixList(Freq_Matrix, N)
X = [1,0]
Y = [2,2]
print SimValue(X, Y, IOF_list, OF_list)
