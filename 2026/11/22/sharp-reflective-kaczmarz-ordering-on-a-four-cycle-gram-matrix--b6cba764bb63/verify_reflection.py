#!/usr/bin/env python3
"""Exact finite symbolic checks for the four-row reflective-Kaczmarz cycle theorem."""
from itertools import permutations
import math
import sympy as S

r=S.symbols('r',real=True)
z=S.symbols('z')
G=S.Matrix([[1 if i==j else r if ((i-j)%4 in (1,3)) else 0
             for j in range(4)] for i in range(4)])
assert S.simplify(G.det()-(1-4*r**2)) == 0
assert G.eigenvals() == {1-2*r:1,1+2*r:1,1:2}
H=[]
for i in range(4):
    M=S.eye(4)
    for j in range(4): M[i,j]-=2*G[i,j]
    assert S.simplify(M.T*G*M-G)==S.zeros(4)
    H.append(M)

cyc=S.expand((z+1)**4-16*r**2*z*(z+1)**2-16*r**4*z*(z-1)**2)
non=S.expand((z+1)**2*((z+1)**2-16*r**2*z))
counts={'cyclic':0,'other':0}
for order in permutations(range(4)):
    P=S.eye(4)
    for i in order: P=H[i]*P
    q=S.expand(P.charpoly(z).as_expr())
    kind='cyclic' if all((order[(i+1)%4]-order[i])%4 in (1,3)
                           for i in range(4)) else 'other'
    assert S.expand(q-(cyc if kind=='cyclic' else non))==0,order
    counts[kind]+=1
assert counts=={'cyclic':8,'other':16}

cp=-1+4*r**2+4*r**4+4*r**3*S.sqrt(r**2+2)
cm=-1+4*r**2+4*r**4-4*r**3*S.sqrt(r**2+2)
ca=-1+8*r**2
assert S.simplify(cp+cm-(-2+8*r**2+8*r**4))==0
assert S.simplify(cp*cm-(1-8*r**2+8*r**4))==0
assert S.simplify(S.diff(cp,r).subs(r,S.Rational(1,2)))==S.Rational(32,3)
assert S.simplify(S.diff(ca,r).subs(r,S.Rational(1,2)))==8
for t in [S.Rational(1,100),S.Rational(1,10),S.Rational(1,4),S.Rational(2,5),S.Rational(49,100)]:
    a,b,c=[float(expr.subs(r,t)) for expr in (cp,cm,ca)]
    assert -1<b<a<c<1,(t,a,b,c)
    gc=math.sqrt(2*(1-a)); ga=math.sqrt(2*(1-c))
    assert gc>ga>0

# Independent Euclidean realizations of the four normalized row vectors.
import numpy as np
for t in [0.125,0.3,0.49]:
    Gr=np.array(G.subs(r,t),dtype=float)
    rows=np.linalg.cholesky(Gr)
    hats=[np.eye(4)-2*np.outer(v,v) for v in rows]
    for order in permutations(range(4)):
        P=np.eye(4)
        for i in order:P=hats[i]@P
        eig=np.linalg.eigvals(P)
        got=min(abs(1-eig))
        cyclic=all((order[(i+1)%4]-order[i])%4 in (1,3) for i in range(4))
        cc=float((cp if cyclic else ca).subs(r,t))
        target=math.sqrt(2*(1-cc))
        assert abs(got-target)<1e-9,(t,order,got,target)
print('PASS: all 24 symbolic spectra, 8 cyclic and 16 noncyclic.')
print('PASS: Gram positivity, reflector isometries, cosine factorization and boundary derivatives.')
print('PASS: five rational gap comparisons and 72 independent numerical Euclidean spectra.')
print('Boundary gap-ratio: 2/sqrt(3) = %.12f'%(2/math.sqrt(3)))
