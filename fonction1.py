# -*- coding: utf-8 -*-
"""
Created on Sat Oct  4 12:18:07 2025

@author: ASUS
"""

def min3(a,b,c):
    if(a<b and a<c):
        m=a
    else:
        if(b<a and b<c):
            m=b
        else:m=c
        return m
def max_min3(a,b,c):
        if(a>b and a>c):
            M=a
            if(b<c):
                m=b
            else:
                m=c
        else:
                if(b>a and b>c):
                    M=b
                    if(a<c):
                        m=a 
                    else:
                         m=c
                else:
                         M=c
                         if(a<b):
                             m=a
                         else:
                             m=b
                         return M,m