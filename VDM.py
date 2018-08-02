# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 17:01:29 2017

@author: Administrator
"""


from math import sqrt
#dissimiliary

def VDM(x, y, Cond_Prob, C):
    #不对称
    dis_vdm = 0.0
    weight = 0.0
    for i in range(C):
        dis_vdm += pow(Cond_Prob[x][i] - Cond_Prob[y][i], 2)
        weight += pow(Cond_Prob[x][i],2)
    return sqrt(weight)*dis_vdm


def MVDM(x, y, Cond_Prob, C):
    dis_mvdm = 0.0
    weight_x = weight_y = 0.0
    for i in range(C):
        dis_mvdm += pow(Cond_Prob[x][i] - Cond_Prob[y][i], 2)
        weight_x += pow(Cond_Prob[x][i],2)
        weight_y += pow(Cond_Prob[y][i],2)
    return sqrt(weight_x*weight_y)*dis_mvdm  


def HEOM(x, y, Cond_Prob, C):
    dis_vdm = 0.0
    for i in range(C):
        dis_vdm += pow(Cond_Prob[x][i] - Cond_Prob[y][i], 2)
    return dis_vdm









Cond_Prob = [[30.0/35,7.0/35,8.0/35],[12.0/60,40.0/60,8.0/60],[4.0/15,2.0/15,9.0/15],[22.0/40,8.0/40,10.0/40]]
print VDM(3, 2, Cond_Prob, 3)
print MVDM(3, 2, Cond_Prob, 3)
        
    
