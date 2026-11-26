#!/usr/bin/env python3
"""Standalone exact-arithmetic check for the characteristic-five Bring fibre."""
import itertools
import sympy as S
u,v,w=S.symbols('u v w')
U=[u,v,w,-u-v-w]
Y=[1+t for t in U]+[S.Integer(1)]
e1=S.expand(sum(Y))
e2=S.expand(sum(a*b for a,b in itertools.combinations(Y,2)))
e3=S.expand(sum(a*b*c for a,b,c in itertools.combinations(Y,3)))
q=-(u*u+u*v+u*w+v*v+v*w+w*w)
c=-(u+v)*(u+w)*(v+w)
assert S.Poly(e1,u,v,w,modulus=5).is_zero
assert S.Poly(e2-q,u,v,w,modulus=5).is_zero
assert S.Poly(e3-3*q-c,u,v,w,modulus=5).is_zero
points=set()
for x in itertools.product(range(5),repeat=3):
    if not any(x):continue
    m=next(t for t in x if t)
    y=tuple(t*pow(m,-1,5)%5 for t in x)
    a,b,d=y
    if (a*a+a*b+a*d+b*b+b*d+d*d)%5==0 and ((a+b)*(a+d)*(b+d))%5==0:
        points.add(y)
assert points=={(1,2,3),(1,2,4),(1,3,2),(1,3,4),(1,4,2),(1,4,3)},points
# In P^3(F5), e1 eliminates X3. Calculate e2 and e3 directly.
projective=[]
for t in itertools.product(range(5), repeat=4):
    if not any(t):continue
    a=next(x for x in t if x)
    pt=tuple(x*pow(a,-1,5)%5 for x in t)
    if pt not in projective:projective.append(pt)
assert len(projective)==156
curve=[]
for t in projective:
    xx=list(t)+[(-sum(t))%5]
    ee2=sum(a*b for a,b in itertools.combinations(xx,2))%5
    ee3=sum(a*b*c for a,b,c in itertools.combinations(xx,3))%5
    if ee2==ee3==0:curve.append(xx)
assert len(curve)==31, len(curve)
# Hilbert series of two homogeneous equations degrees 2 and 3 in 3 variables.
from math import comb
h=lambda n: comb(n+2,2)-(comb(n,2) if n>=2 else 0)-(comb(n-1,2) if n>=3 else 0)+(comb(n-3,2) if n>=5 else 0)
assert [h(n) for n in range(8)]==[1,3,5,6,6,6,6,6]
assert sum(6-h(n) for n in range(3))==9
print('VERIFY_OK: chart equations, six rational lines, 31 rational points, delta 9')
