# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 17:58:49 2025

@author: ASUS
"""

import numpy as np
def serie_statistique(x,n):
    N=sum(n)
    p=len(x)
    S1=0
    for i in range(0,p):
        S1=S1+n[i]*x[i]
        m=S1/N
        S2=0
    for i in range(0,p):
            S2=S2+n[i]*(x[i]**2)
    V=(S2/N)-(m**2)
    e=np.sqrt(V)
    return m,V,e
x=np.array([12,14,18,20,25])
n=np.array([80,70,140,60,48])
m,V,e=serie_statistique(x,n)
print("moyenne:",m)
print("variance:",V)
print("écart type:",e)