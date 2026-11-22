"""Exact-rational certificate for a three-phenotype sequencing reversal.

Run with Python 3 standard library: python checker.py
No biological data are used; this only checks the displayed matrices.
"""
from fractions import Fraction as F
from math import factorial

N = 40
Q = [[-1,1,0],[1,-2,1],[0,1,-1]]
A = [[Q[i][j]-(1 if i==j==2 else 0) for j in range(3)] for i in range(3)]
B = [[Q[i][j]-(1 if i==j==1 else 0) for j in range(3)] for i in range(3)]

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]

def add(A,B):
    return [[A[i][j]+B[i][j] for j in range(3)] for i in range(3)]

def eye():
    return [[F(i==j) for j in range(3)] for i in range(3)]

def series(M,t):
    E=eye(); P=eye()
    for k in range(1,N+1):
        P=mm(P,M)
        P=[[x*t/k for x in row] for row in P]
        E=add(E,P)
    return E

def delta(t):
    EA, EB = series(A,t), series(B,t)
    AB, BA=mm(EA,EB),mm(EB,EA)
    # Initial e1, terminal readout all-phenotype count.
    d=sum(BA[i][0]-AB[i][0] for i in range(3))
    eps=F(256)*F(5)**(N+1)/factorial(N+1)
    # e^5<256, and ||A||_inf<=4, ||B||_inf<=5, t<=1.
    # Bound each product's truncation error by 512 eps+eps^2;
    # multiply by 2 for both orders and 3 for total-population readout.
    error=6*(512*eps+eps*eps)
    assert abs(d)>error
    return d, error

assert A==[[-1,1,0],[1,-2,1],[0,1,-2]]
assert B==[[-1,1,0],[1,-3,1],[0,1,-1]]
for t,sgn in [(F(1,5),-1),(F(1),+1)]:
    d,e=delta(t)
    assert (d>0)-(d<0)==sgn
    print('t=',t, 'Taylor difference=',float(d), 'absolute error bound=',float(e), 'certified sign=',sgn)
print('PASS: signs rigorously certified with rational arithmetic and analytic Taylor remainder.')
