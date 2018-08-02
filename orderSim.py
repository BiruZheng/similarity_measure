# -*- coding: utf-8 -*-
"""
Created on Sat Jul 08 15:16:39 2017

@author: Administrator
"""
from math import log 
import numpy as np
import pandas as pd


#Lin Similarity
def LinSim(i, j, frequency, order):
    if i == j:
        return 1
    elif order == True:
        #odernal Values
        sim = 2 * log(sum(frequency[i:j+1] if i < j else frequency[j:i+1]), 2)
    else:
        sim = 2 * log(frequency[i] + frequency[j], 2)
    return sim/(log(frequency[i], 2) + log(frequency[j], 2))
    
    


#Similarity between Ordinal Values TO the matrix
def LinSimMat(frequency, order):
    n = len(frequency)
    LinSimM = np.zeros((n, n))
    for i in range(n):
        for j in range(i,n):
            LinSimM[i][j] = LinSim(i, j, frequency, order)
            LinSimM[j][i] = LinSimM[i][j]
    return LinSimM


#test
A = [0.05, 0.1, 0.5, 0.2, 0.15]
#print LinSim(0, 1, A, order = True)

BLFX = [0.053, 0.304, 0.582, 0.061]

level = [0.3, 0.33, 0.37]

LinSimMat(level, False)

#print LinSimMat(BLFX, order = True)


#print LinSimMat(level, order = True)
#print LinSimMat(BLFX, order = False)

education = [0.002,0.005,0.01,0.018,0.015,0.027,0.035,0.013,0.326,0.221,0.043,0.033,0.167,0.054,0.018,0.012]
#Sim = LinSimMat(education, order = True)

#dataframe = pd.DataFrame(Sim)

#dataframe.to_csv('SimEducation.csv')
'''===================================================================='''

df = pd.read_csv('iris_data.csv')
#数据框的协方差
data = df.values[:,:-1]
covD = df.cov()
invD = np.linalg.inv(covD)


#Mahalanobis distance

def MahaDist(i, j, data, invD):
    if i == j:
        return 0
    else:
        x = data[i] - data[j]
        return np.sqrt(np.dot(np.dot(x,invD),x.T))

'''
def MahaDistMat(data, invD):
    n = data.shape[0]
    MahaDistM = np.zeros((n,n))
    for i in range(n):
        for j in range(i,n):
            MahaDistM[i][j] = MahaDist(i,j,data,invD)
            MahaDistM[j][i] = MahaDistM[i][j]
    return MahaDistM


#test
print MahaDist(60,130,data,invD)
'''

'''===================================================================='''


#print MahaDist(2,4,data, invD)

def EucDist(i, j, data):
    if i == j:
        return 0
    else:
        return np.sqrt(np.sum(np.square(data[i]-data[j])))

'''
def EucDistMat(data):
    n = data.shape[0]
    EucDistM = np.zeros((n,n))
    for i in range(n):
        for j in range(i,n):
            EucDistM[i][j] = EucDist(i, j, data)
            EucDistM[j][i] = EucDistM[i][j]
    return EucDistM

#test
print EucDist(60,130,data)
'''

'''===================================================================='''

#Manhattan Distance

def ManhaDist(i, j, data):
    if i == j:
        return 0
    else:
        return np.sum(np.abs(data[i]-data[j]))

'''    
def ManhaDistMat(data):
    n = data.shape[0]
    ManhaDistM = np.zeros((n,n))
    for i in range(n):
        for j in range(i,n):
            ManhaDistM[i][j] = ManhaDist(i, j, data)
            ManhaDistM[j][i] = ManhaDistM[i][j]
    return ManhaDistM
'''


'''===================================================================='''

#Chebyshev Distance

def CheDist(i, j, data):
    if i == j:
        return 0
    else:
        return np.max(np.abs(data[i]-data[j]))

'''===================================================================='''

# Distance matrix 
def DistMat(data, method):
    n = data.shape[0]
    DistM = np.zeros((n,n))
    for i in range(n):
        for j in range(i,n):
            DistM[i][j] = method(i, j, data)
            DistM[j][i] = DistM[i][j]
    return DistM


#test
x = np.random.random(10)
y = np.random.random(10)

X = np.vstack([x,y])
data = X.T

#print DistMat(data, CheDist)


'''===================================================================='''

#Kullback-Leibler Divergence
def KLDive(i, j, frequency):
    if i == j:
        return 0
    else:
        return frequency[i]*log(frequency[i]/frequency[j], 2)


#Jensen-Shannon Divergence   
def JSDive(i, j, frequency):
    return (KLDive(i, j, frequency) + KLDive(j, i, frequency))/2

# Jensen-Shannon Divergence matrix
def JSDiveMat(frequency):
    n = len(frequency)
    JSDiveM = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            JSDiveM[i][j] = JSDive(i, j, frequency)
            JSDiveM[j][i] = JSDiveM[i][j]
    return JSDiveM


#test
#tryit = JSDiveMat(BLFX)

#tryit2 = JSDiveMat(level)

'''===================================================================='''
#modify of Lin

Arate = np.array([[0.2, 0.1, 0.6],
                  [0.15, 0.7, 0.15],
                  [0.65, 0.2, 0.25]])
    

def MLinSim(i, j, Arate):
    if i == j:
        return 1;
    else:
        sim = 0
        for k in range(3):
            sim = sim + 2*log(Arate[i][k] + Arate[j][k],2)/(log(Arate[i][k],2)+log(Arate[j][k],2))
        return sim/3
 

def MLinSim2(i, j, Arate):
    if i == j:
        return 1
    else:
        return sum(map(lambda x,y:2*log(x+y,2)/(log(x,2)+log(y,2)),\
                       Arate[i],Arate[j]))/3

#test
MLinSim2(0,1,Arate)

def MLinSimMat(rate):
    n = rate.shape[0]
    MLinSimM = np.zeros((n,n))
    for i in range(n):
        for j in range(i,n):
            MLinSimM[i][j] = MLinSim2(i, j, rate)
            MLinSimM[j][i] = MLinSimM[i][j]
    return MLinSimM

MLinSimMat(Arate)

