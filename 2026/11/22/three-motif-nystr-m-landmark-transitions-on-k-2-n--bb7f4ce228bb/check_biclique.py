#!/usr/bin/env python3
"""Exact independently replayable tests for rank-two Nyström on K_{2,n}."""
from fractions import Fraction
from itertools import combinations
import sympy as sp

x,n=sp.symbols('x n',positive=True)
D_A=(x+2)/(x*(x+n)*(x+n+2))
D_B=(x*x+(n+2)*x+4)/(x*(x+2)**2*(x+n+2))
D_C=(x+1)*(x+n+1)/(x*(x+2)*(x+n)*(x+n+2))
D=(D_A,D_B,D_C)
C=[-sp.diff(d,x)/d for d in D]
P=(n-2)*x**4+2*(n*n-n-1)*x**3+n*(n*n+2)*x*x+8*(2*n-1)*x-2*(n**3-3*n*n-4*n+4)
assert sp.factor(C[0]-C[1]+2*(n-2)*(x*x+n*x-n+2)/((x+n)*(x+2)*(x*x+(n+2)*x+4)))==0
assert sp.factor(C[0]-C[2]-(2-(n-2)*x)/((x+1)*(x+2)*(x+n+1)))==0
assert sp.factor(C[1]-C[2]-P/((x+n)*(x+1)*(x+2)*(x+n+1)*(x*x+(n+2)*x+4)))==0
assert sp.factor((x*x+n*x-n+2).subs(x,2/(n-2)) + (n**3-8*n*n+16*n-12)/(n-2)**2)==0

checks=4
for NN in range(3,13):
    N=NN+2
    L=sp.zeros(N,N)
    for i in range(2):
        for j in range(2,N):
            L[i,i]+=1;L[j,j]+=1;L[i,j]-=1;L[j,i]-=1
    for MU in [sp.Rational(1,10),sp.Rational(1,2),sp.Rational(1,1),sp.Rational(3,1)]:
        G=(MU*sp.eye(N)+L).inv()
        H=G*G
        observed=[]
        for pair in [(0,1),(2,3),(0,2)]:
            W=G.extract(pair,pair)
            T=H.extract(pair,pair)
            observed.append(sp.trace(W.inv()*T))
        for k in range(3):
            assert sp.factor(observed[k]-C[k].subs({n:NN,x:MU}))==0
            assert sp.factor(G.extract([(0,1),(2,3),(0,2)][k],[(0,1),(2,3),(0,2)][k]).det()-D[k].subs({n:NN,x:MU}))==0
            checks+=2
        if NN<=8:
            for pair in combinations(range(N),2):
                W=G.extract(pair,pair)
                capture=sp.trace(W.inv()*H.extract(pair,pair))
                typ=0 if pair[1]<2 else (1 if pair[0]>=2 else 2)
                assert sp.factor(capture-observed[typ])==0
                checks+=1
        best=max(observed)
        assert best==max(C[k].subs({n:NN,x:MU}) for k in range(3))
        checks+=1
    if NN>=4:
        # strictly one sign variation of P for all integer NN>=4
        coefficients=[NN-2, 2*(NN*NN-NN-1), NN*(NN*NN+2),8*(2*NN-1),-2*(NN**3-3*NN*NN-4*NN+4)]
        assert all(z>0 for z in coefficients[:-1]) and coefficients[-1]<0
    else:
        assert all(z>0 for z in [NN-2,2*(NN*NN-NN-1),NN*(NN*NN+2),8*(2*NN-1),-2*(NN**3-3*NN*NN-4*NN+4)])
    checks+=1
print(f'PASS: {checks} exact symbolic/rational assertions; no floating-point significance decisions')
