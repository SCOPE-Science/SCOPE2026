#!/usr/bin/env python3
"""Independent Gauss-Legendre integration of the pentagon double moments.
The 14x14 tensor rule is exact for the Duffy-transformed polynomial kernel
at all even powers from 6 through 24, up to floating-point summation error.
"""
import numpy as np
from math import sqrt
c=(sqrt(5)-1)/4;d=-(sqrt(5)+1)/4;q=(sqrt(5)-1)/2
lam=(5+sqrt(5))/8
vertices=np.array([[1,0],[c,1],[d,q],[d,-q],[c,-1]],float)
nodes,gw=np.polynomial.legendre.leggauss(14)
nodes=(nodes+1)/2;gw=gw/2
p=[];w=[]
for i in range(5):
 a,b=vertices[i],vertices[(i+1)%5]
 det=np.linalg.det(np.vstack([a,b]))
 for k,u in enumerate(nodes):
  for l,v in enumerate(nodes):
   p.append(u*a+(1-u)*v*b)
   w.append(gw[k]*gw[l]*(1-u)*det)
p=np.asarray(p);w=np.asarray(w)
assert abs(w.sum()-2.5)<1e-12
r2=(p[:,None,0]-p[None,:,0])**2+lam*(p[:,None,1]-p[None,:,1])**2
W=w[:,None]*w[None,:]
reference={3:10.205776150297249,12:24947.406885104232}
for m in (3,12):
 E=np.sum(W*r2**m)
 diff=abs(E-reference[m])/reference[m]
 print('m=%d: independent quadrature E=%.13g; relative agreement %.4g'%(m,E,diff))
 assert diff<1e-11
print('INDEPENDENT_QUADRATURE_PASS')
