#!/usr/bin/env python3
"""Exact certificate for 24 flexes and cyclotomic splitting of a plane quartic.
Run using Python 3 with SymPy 1.13 or later.
"""
import sympy as s
from math import gcd
x, y, z, X, Y, Z = s.symbols('x y z X Y Z')
phi = s.cyclotomic_poly(7, z)
F = X**3 * Y + Y**3 * Z + Z**3 * X
H = X**5*Z - 5*X**2*Y**2*Z**2 + X*Y**5 + Y*Z**5
assert s.expand(s.det(s.hessian(F,(X,Y,Z))) + 54*H) == 0
for point in [(1,0,0),(0,1,0),(0,0,1)]:
    assert F.subs(dict(zip((X,Y,Z),point))) == 0
    assert H.subs(dict(zip((X,Y,Z),point))) == 0
f = s.expand(F.subs({X:x,Y:y,Z:1}))
h = s.expand(H.subs({X:x,Y:y,Z:1}))
pairs = [(z**3+z**4, z**2+z**3+z**4+z**5),
         (1+z**4,z+z**2+z**4+z**5),
         (z**5+z**4,1+z+z**2+z**3),
         (z**5+z**3,1+z**2+z**3+z**5)]
assert all(s.rem(s.expand(f.subs({x:a,y:b})),phi,z) == 0 and
           s.rem(s.expand(h.subs({x:a,y:b})),phi,z) == 0 for a,b in pairs)
q3=x**3+x**2-2*x-1
q6a=x**6-5*x**5+11*x**4-13*x**3+9*x**2-3*x+1
q6b=x**6+2*x**5+4*x**4+x**3+2*x**2-3*x+1
q6c=x**6+2*x**5+4*x**4+8*x**3+9*x**2+4*x+1
polys=[x,q3,q6a,q6b,q6c]
assert s.expand(s.resultant(f,h,y)+s.prod(polys))==0
for i,(a,b) in enumerate(pairs):
    assert s.expand(s.resultant(phi,x-a,z)-polys[i+1]**(2 if i==0 else 1))==0
for polynomial in polys[1:]:
    assert s.factor_list(polynomial)[1] == [(polynomial, 1)]
    disc=int(s.discriminant(polynomial,x))
    assert all(q in (2,7) for q in s.factorint(abs(disc)))
assert [int(s.discriminant(v,x)) for v in polys[1:]] == [49,-7**5,-2**6*7**5,-2**6*7**5]
for i, p in enumerate(polys):
    for q in polys[i+1:]:
        res=abs(int(s.resultant(p,q,x)))
        assert all(k in (2,7) for k in s.factorint(res))
# The actual conjugate x coordinates have exact cycles of length 3,6,6,6.
# Their pairwise disjointness and degree sum 1+3+6+6+6=22,
# plus two coordinate points at infinity, prove completeness by Bezout.
# Frobenius on zeta_7 is z -> z^p, and permutation cycle count follows.
for r in (1,2,3,4,5,6):
    cycles=[1]*3
    for j,(a,b) in enumerate(pairs):
        vals=[]
        for k in range(6):
            t=pow(r,k,7)
            vals.append(tuple(int(v) for v in s.Poly(s.rem(a.subs(z,z**t),phi,z),z).all_coeffs()))
        # normalize tuples to length six, necessary for robust equality
        vals=[(0,)*(6-len(t))+t for t in vals]
        d=next((d for d in range(1,7) if vals[d%6]==vals[0]),None)
        assert d is not None
        cycles.extend([d]*([3,6,6,6][j]//d))
    counts={d:cycles.count(d) for d in set(cycles)}
    expected={1:{1:24},6:{1:6,2:9},2:{1:3,3:7},4:{1:3,3:7},3:{1:3,3:1,6:3},5:{1:3,3:1,6:3}}[r]
    assert counts==expected, (r,counts,expected)
print('KLEIN_FLEX_CYCLOTOMIC_CERTIFIED_OK')
