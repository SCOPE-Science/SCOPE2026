#!/usr/bin/env python3
"""Deterministic numerical diagnostics for Steiner-inellipse eccentricity tails.
Only proves the finite checks it performs; the analytic proof is separate.
"""
import numpy as np
from math import pi,sqrt
from scipy.stats import qmc

def shape(theta2, theta3):
    z2=np.exp(1j*theta2); z3=np.exp(1j*theta3)
    a=np.abs(1-z2); b=np.abs(z2-z3); c=np.abs(z3-1)
    ss=a*a+b*b+c*c
    k=np.divide(sqrt(3)*a*b*c,ss, out=np.zeros_like(ss),where=ss>0)
    k=np.clip(k,0,1)
    r=k/(1+np.sqrt(np.maximum(0,1-k*k)))
    e=np.sqrt(np.maximum(0,1-r*r))
    return r,e,k

def direct_matrix(u,v):
    p=np.stack([np.cos([0,u,v]),np.sin([0,u,v])],axis=1)
    cen=p.mean(axis=0)
    cov=(p-cen).T@(p-cen)
    vals=np.linalg.eigvalsh(cov)
    return sqrt(max(vals[0],0)/vals[1])

for i in range(1,1001):
    u=pi*(sqrt(2)*i%2);v=pi*(sqrt(3)*i%2)
    r=shape(np.array(u),np.array(v))[0]
    assert abs(r-direct_matrix(u,v))<5e-8,(u,v,r,direct_matrix(u,v))

# Linear local differentials: fixed third angular separation.
for t in (0.1,0.6,1.5,2.9,4.3,6.1):
    q=shape(np.array(1e-6),np.array(t))[0]/1e-6
    assert abs(q-sqrt(3)/4)<2e-4, (t,q)

p_circ=3*sqrt(3)/(16*pi)
p_flat=4*sqrt(3)/pi
n=2**22
sob=qmc.Sobol(d=2,scramble=False)
xy=sob.random_base2(m=22)
r,e,k=shape(2*pi*xy[:,0],2*pi*xy[:,1])
print('Near-circle coefficient',p_circ,'near-flat ratio coefficient',p_flat)
for eps in (0.45,0.3,0.2,0.14):
    prob=np.mean(e<eps)
    print('e<',eps,'prob',prob,'scaled',prob/eps**4,'ratio to theory',prob/(p_circ*eps**4))
for eta in (0.1,0.04,0.02,0.01):
    prob=np.mean(r<eta)
    print('r<',eta,'prob',prob,'scaled',prob/eta,'ratio',prob/(p_flat*eta))
# Dirichlet/Ellipse local domain scaling along equilateral orientations.
for h in (1e-2,1e-3,1e-4):
    U,V=0.29,-0.20
    _,e,_=shape(np.array(2*pi/3+h*U),np.array(4*pi/3+h*V))
    ratio=(e*e/h)/(4/3*sqrt(U*U+V*V-U*V))
    print('linearized eccentricity-square ratio',h,ratio)
print('finite checks passed')
