#!/usr/bin/env python3
"""Reproduce exact three-projection cost identities and marginal-optimality certificate."""
import itertools
from fractions import Fraction
import sympy as sp
q=sp.symbols('q',real=True,positive=True)
s=sp.sqrt(q); w=sp.sqrt(1-2*q)
U=[sp.Matrix([1,0,0]),sp.Matrix([s,s,w]),sp.Matrix([0,1,0])]
P=[sp.eye(3)-u*u.T for u in U]
idx=list(itertools.product(range(3),repeat=3))
cs=[]
for i,j,k in idx:
 S=P[k]*P[j]*P[i]
 c=sp.simplify(sp.trace(S.T*S))
 cs.append(c)
 a=[q/2,q,q/2]
 bound=a[i]+a[j]+a[k]+(q**2 if j==1 else 0)
 d=sp.factor(c-bound)
 assert sp.simplify(d)==0 if len({i,j,k})==3 else sp.simplify(d.subs(q,sp.Rational(1,4)))>0,(i,j,k,d)
 assert (len({i,j,k})==3) == (d==0)
assert len(idx)==27
avg=sp.factor(sum(cs)/27)
assert avg.subs(q,sp.Rational(1,4))==sp.Rational(235,216),avg
perm=[v for v in idx if len(set(v))==3]
cavg=sp.factor(sum(cs[idx.index(v)] for v in perm)/6)
assert sp.simplify(cavg-(2*q+q*q/3))==0,(cavg,q)
A=sp.Matrix([[int(v[r]==i) for v in perm] for r in range(3) for i in range(3)])
assert A.rank()==5
v=sp.symbols('v',real=True)
p=sp.Matrix([sp.Rational(1,3)-v,v,v,sp.Rational(1,3)-v,sp.Rational(1,3)-v,v])
assert A*p==sp.ones(9,1)/3
assert (2*q+q*q/3).subs(q,sp.Rational(1,4))==sp.Rational(25,48)
assert sp.Rational(235,216)-sp.Rational(25,48)==sp.Rational(245,432)
print('PASS: all 27 symbolic cost formulas, strict repeat slacks at q=1/4, 9 marginal equalities, exact independence and graph values')
