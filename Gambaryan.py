# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 15:51:14 2017

@author: Administrator
"""


from math import log 
import numpy as np


def GambaryanSim(i, j, prob):
    if i != j:
        sim = 0.0
    else:
        sim = -(prob[i]*log(prob[i],2)+(1-prob[i])*log(1-prob[i],2))
    return sim


def GambaryanMatrix(prob):
    n = len(prob)
    Sim_Matrix = np.zeros((n,n))
    for i in range(n):
        for j in range(i, n):
            Sim_Matrix[i][j] = GambaryanSim(i, j, prob)
            Sim_Matrix[j][i] = Sim_Matrix[i][j]
    return n, Sim_Matrix


def GambaryanMatrix_list(prob_Matrix):
    d = len(prob_Matrix)
    Gambaryan_list = []
    sum_n = 0.0
    for i in range(d):
        n, Sim_Matrix = GambaryanMatrix(prob_Matrix[i])
        Gambaryan_list.append(Sim_Matrix)
        sum_n += n
    return sum_n, Gambaryan_list


def GambaryanValue(X, Y, sum_n, Gambaryan_list):
    d = len(X)
    sim = 0.0
    for i in range(d):
        sim += Gambaryan_list[i][X[i],Y[i]]
    return sim/sum_n


prob_Matrix = [[0.35,0.54,0.11]]
sum_n, Gambaryan_list = GambaryanMatrix_list(prob_Matrix)
X = [0]
Y = [0]
print GambaryanValue(X, Y, sum_n, Gambaryan_list)
