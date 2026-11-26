#!/usr/bin/env python3
"""Exact certificate for the Klein quartic flex-divisor Frobenius theorem.
Requires sympy (tested with 1.14), Python 3; no external data or network.
"""
import sympy as s
from itertools import combinations
x,y,z,t=s.symbols('x y z t')
f=x**3*y+y**3*z+z**3*x
h=x**5*z-5*x**2*y**2*z**2+x*y**5+y*z**5
assert s.expand(s.hessian(f,(x,y,z)).det()+54*h)==0
F=s.expand(f.subs(z,1));B=s.expand(h.subs(z,1))
P=[x**3+x**2-2*x-1,
   x**6-5*x**5+11*x**4-13*x**3+9*x**2-3*x+1,
   x**6+2*x**5+4*x**4+x**3+2*x**2-3*x+1,
   x**6+2*x**5+4*x**4+8*x**3+9*x**2+4*x+1]
R=s.expand(x*s.prod(P))
assert s.expand(s.resultant(F,B,y)+R)==0
assert s.factorint(abs(s.discriminant(R,x)))=={2:42,7:77}
C=sum(t**i for i in range(7))
E=[t**3+t**4,1+t**4,t**4+t**5,t**3+t**5]
for poly,expr in zip(P,E):
    assert s.rem(poly.subs(x,expr),C,t)==0
# The 24 Hessian intersections have two transverse points at infinity,
# one affine rational origin, plus roots of the 21-degree squarefree factor.
# Every affine resultant root corresponds to just one intersection point,
# since degree 22 equals the Bezout 24 minus two infinity points.
# Compare direct F_p point counts and factor degrees with the predicted cycles.
for p in [5,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]:
    assert p!=7
    n=3
    for u in range(p):
        for v in range(p):
            if (u**3*v+v**3+u)%p==0 and (u**5-5*u*u*v*v+u*pow(v,5,p)+v)%p==0:
                if (u,v)!=(0,0):n+=1
    degrees=[]
    for poly in P:
        for g,m in s.factor_list(poly,modulus=p)[1]:
            degrees.extend([s.degree(g,x)]*m)
    if p%7==1: expected=[1]*21
    elif p%7==6: expected=[1]*3+[2]*9
    elif p%7 in (2,4):expected=[3]*7
    else: expected=[3]+[6]*3
    assert sorted(degrees)==sorted(expected), (p,degrees,expected)
    assert n==3+degrees.count(1), (p,n,degrees)
print('KLEIN_24_FLEX_CYCLOTOMIC_FROBENIUS_VERIFIED')
