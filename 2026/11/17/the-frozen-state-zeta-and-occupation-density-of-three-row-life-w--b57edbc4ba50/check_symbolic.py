#!/usr/bin/env python3
"""Exact transfer and spectral checks for three-row Life without Death."""
from math import comb
from collections import deque
import sympy as s
x,z,u=s.symbols('x z u')
T=s.zeros(16)
for a in range(4):
    for b in range(4):
        for c in range(4):
            if b==3 or a+b+c!=3:
                T[4*a+b,4*b+c]=comb(3,c)
P=s.factor(T.charpoly(x).as_expr())
D=s.factor((s.eye(16)-z*T).det())
expected=x**5*(x**11-5*x**10-15*x**9-26*x**8+162*x**7+528*x**6+261*x**5-1188*x**4-4131*x**3-3888*x**2-1458*x+2187)
assert s.expand(P-expected)==0
print('characteristic =',P)
print('zeta denominator =',D)
# Check strong connectivity and a loop. This makes the nonnegative transfer primitive.
def reachable(start):
    visited={start}; q=deque([start])
    while q:
        v=q.popleft()
        for w in range(16):
            if T[v,w]!=0 and w not in visited:
                visited.add(w);q.append(w)
    return visited
assert all(len(reachable(i))==16 for i in range(16))
assert T[15,15]==1
print('strongly connected = yes; self-loop at (3,3) = yes')
# Exact Perron certificate. The entries are rational and strictly positive.
V=[5405164742176,4535317645990,6245655706778,10000000000000,
   4154114605937,5839737756392,8876300210490,10000000000000,
   4888826766745,7753492068752,9576333449524,10000000000000,
   6063101208700,8348321552729,9576333449524,10000000000000]
ratios=[s.Rational(sum(int(T[i,j])*V[j] for j in range(16)),V[i]) for i in range(16)]
lo,hi=min(ratios),max(ratios)
assert s.Rational(6983706,1000000)<lo and hi<s.Rational(6983708,1000000)
print('Collatz lower =',lo,'upper =',hi)
print('Perron bracket decimal =',float(lo),float(hi))
# Polynomial density-resolved trace, with the multiplicities of every column weight.
U=s.zeros(16)
for a in range(4):
    for b in range(4):
        for c in range(4):
            if b==3 or a+b+c!=3:
                U[4*a+b,4*b+c]=comb(3,c)*u**c
Pmat=s.eye(16)
for n in range(1,8):
    Pmat=Pmat*U
    if n>=3:
        Q=s.Poly(s.trace(Pmat),u)
        print('n=',n,'count=',sum(Q.all_coeffs()),'histogram=',[Q.nth(j) for j in range(3*n+1)])
assert s.expand(s.trace(U**3).subs(u,1)-428)==0
assert s.expand(s.trace(U**7).subs(u,1)-811242)==0
print('unweighted counts n=3..16:',[(n,int(s.trace(T**n))) for n in range(3,17)])
# The weighted transfer gives the frozen-state occupation density by
# differentiating the simple Perron eigenvalue. No finite-n extrapolation.
Du=s.factor((s.eye(16)-z*U).det(method='domain-ge'))
root=s.nsolve(expected/x**5,6.98,prec=45)
Z=s.N(1/root,45)
mean_column=s.N((s.diff(Du,u)/(z*s.diff(Du,z))).subs({z:Z,u:1}),30)
density=mean_column/3
assert 0.58228645<float(density)<0.58228646
print('limit occupied fraction =',density)
