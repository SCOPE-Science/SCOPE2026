#!/usr/bin/env python3
"""Independent finite numerical checks for an analytic matrix-function bound."""
import math
import numpy as np
from numpy.linalg import matrix_power, inv
rng=np.random.default_rng(217)
checks=0
for n in range(1,10):
    c=(1+math.sqrt(n))/2
    q=(1+1/math.sqrt(n))/2
    u=np.ones(n)
    u[0]=math.sqrt(q)
    if n>1: u[1:]=math.sqrt((1-q)/(n-1))
    P=np.outer(u,u); J=np.ones((n,n)); I=np.eye(n)
    assert abs(np.sum(np.abs(P[0]))-c)<1e-10;checks+=1
    for k in range(2,8):
        deriv=sum(matrix_power(P,j)@J@matrix_power(P,k-1-j) for j in range(k))
        assert abs(deriv[0,0]-(2*c+(k-2)*c*c))<2e-10;checks+=1
    b=.4
    R=inv(I-b*P)
    assert abs((R@J@R)[0,0]-(1+c*b/(1-b))**2)<1e-10;checks+=1
    for _ in range(12):
        G=rng.normal(size=(n,n)); G=(G+G.T)/2
        vals,V=np.linalg.eigh(G)
        A=(V*np.clip((vals+3)/(max(1,n)+6),.01,.9))@V.T
        H=rng.normal(size=(n,n)); H=(H+H.T)/2
        vals,V=np.linalg.eigh(H)
        B=(V*np.clip((vals+3)/(max(1,n)+6),.01,.9))@V.T
        for k in (2,3,5):
            actual=np.max(np.abs(matrix_power(A,k)-matrix_power(B,k)))/max(1e-12,np.max(np.abs(A-B)))
            assert actual<=2*c+(k-2)*c*c+3e-10;checks+=1
        actual=np.max(np.abs(inv(I-b*A)-inv(I-b*B)))/max(1e-12,np.max(np.abs(A-B)))
        assert actual <=(1+c*b/(1-b))**2+3e-10;checks+=1
print(f"PASS {checks} checks")
