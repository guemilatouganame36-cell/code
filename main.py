# -*- coding: utf-8 -*-
"""
Created on Sat Oct  4 12:20:35 2025

@author: ASUS
"""

import fonction1 as op
a=float(input("donner la valeur de a:"))
b=float(input("donner la valeur de b:"))
c=float(input("donner la valeur de c:"))
m=op.min3(a,b,c)
M,m=op.max_min3(a,b,c)
print("le minimum de",a,b,"et",c,"est:",m)
print("le minimum et le maximum de",a,b,"et",c,"est",m,"et",M)