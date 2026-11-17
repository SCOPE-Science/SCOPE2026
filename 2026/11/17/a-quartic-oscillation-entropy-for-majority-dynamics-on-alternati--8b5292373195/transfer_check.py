#!/usr/bin/env python3
"""Exact integer transfer and spectral checks for alternating leaf-decorated cycles."""
import sympy as sp
from math import isclose

bits = [(0,0),(0,1),(1,0),(1,1)]
pair_states = [(a,b) for a in range(4) for b in range(4)]

def majority(a,b,c):
    return int(a+b+c>=2)

def transfer(decorated):
    A=sp.zeros(16,16)
    for i,(p,q) in enumerate(pair_states):
        for j,(qq,r) in enumerate(pair_states):
            if q!=qq: continue
            al,bl=bits[p]; a,b=bits[q]; ar,br=bits[r]
            if decorated:
                valid=(b==al or b==ar) and (a==bl or a==br)
            else:
                valid=(b==majority(al,a,ar) and a==majority(bl,b,br))
            if valid: A[i,j]=1
    return A

D=transfer(True)
U=transfer(False)
M=D*U
z=sp.symbols('z')
assert sp.factor(M.charpoly(z).as_expr()) == z**6*(z-1)*(z**2+1)*(z**3+2*z**2+4*z+1)*(z**4-5*z**3+4*z**2-z-1)
R=sp.zeros(4,4)
for i,(a,b) in enumerate(bits):
    for j,(c,d) in enumerate(bits):
        if b==c and (b==a or b==d):R[i,j]=1
assert sp.factor(R.charpoly(z).as_expr()) == (z*z-z-1)*(z*z-z+1)

P=sp.eye(16); Q=sp.eye(4)
print('m, fixed configurations, two-step configurations, primitive two-cycle orbits')
for m in range(1,13):
    P=P*M; Q=Q*R*R
    p=int(sp.trace(P));f=int(sp.trace(Q))
    assert (p-f)%2==0 and p>=f
    print(m,f,p,(p-f)//2)
print('CHARACTERISTIC_POLYNOMIALS_OK')
print('TRANSFER_INTEGERS_OK')
