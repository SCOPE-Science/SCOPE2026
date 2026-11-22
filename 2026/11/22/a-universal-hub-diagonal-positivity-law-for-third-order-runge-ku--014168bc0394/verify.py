"""Exact-rational reproducibility checks for third-order Taylor steps on weighted stars.
Run with Python 3: python verify.py. No dependencies beyond standard library.
"""
from fractions import Fraction as F
from itertools import product
from math import isclose

checks = 0

def matmul(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def test(weights):
    global checks
    m=len(weights)
    n=m+1
    S=sum(weights)
    T2=sum(x*x for x in weights)
    T3=sum(x*x*x for x in weights)
    Q=[[F(0) for j in range(n)] for i in range(n)]
    Q[0][0]=-S
    for i,a in enumerate(weights,1):
        Q[0][i]=Q[i][0]=a
        Q[i][i]=-a
    Q2=matmul(Q,Q);Q3=matmul(Q2,Q)
    for h in [F(0),F(1,7*S),F(1,S),F(5,4*S),F(3,2*S),F(2,S),F(7,2*S)]:
        P=[[F(i==j)+h*Q[i][j]+h*h*Q2[i][j]/2+h*h*h*Q3[i][j]/6 for j in range(n)] for i in range(n)]
        center=1-S*h+(S*S+T2)*h*h/2-(S**3+2*S*T2+T3)*h**3/6
        assert P[0][0]==center
        for i,a in enumerate(weights,1):
            leaf=1-a*h+a*a*h*h-a*a*(S+3*a)*h**3/6
            cross=a*h*(1-(S+a)*h/2+(S*S+T2+S*a+a*a)*h*h/6)
            assert P[i][i]==leaf and P[0][i]==cross
            assert P[i][i] >= P[0][0]
            if h>0 and m>=2: assert P[i][i]>P[0][0]
            if h>0: assert P[0][i]>0
            for j,b in enumerate(weights,1):
                if i==j: continue
                pair=a*b*h*h*(3-(S+a+b)*h)/6
                assert P[i][j]==pair
        assert all(sum(row)==1 for row in P)
        checks+=n*n

for m in range(1,7):
    for tup in product((F(1),F(2),F(3)),repeat=m):
        test(tup)
for m in (7,8,9):
    for seed in range(10):
        ws=[F((seed+3*i)%7+1, 3+(i%3)) for i in range(m)]
        test(ws)
print('VERIFY_OK',checks,'exact-entry/row identity groups')
