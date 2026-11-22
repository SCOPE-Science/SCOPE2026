#!/usr/bin/env python3
"""Finite rational tests of the stated complete-bipartite inball theorem.

Requires Python 3 and SymPy. The unrestricted result is proved in RESULT.md;
these calculations are independent finite corroboration, not a proof by census.
"""
from itertools import product
from fractions import Fraction as F
from math import comb
import sympy as S


def centered(raw):
    v = [F(v) for v in raw]
    mu = sum(v) / len(v)
    return tuple(x-mu for x in v)


def normals(p,q):
    n=p+q
    A={centered(e+(0,)*q) for e in product((-1,1), repeat=p)}
    B={centered((0,)*p+e) for e in product((-1,1), repeat=q)}
    return A | B


def roots(p,q):
    n=p+q
    ans=[]
    for i in range(p):
        for j in range(q):
            e=[0]*n
            e[i]=1;e[p+j]=-1
            ans.append(tuple(e));ans.append(tuple(-x for x in e))
    return ans


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def rank(vs):
    return S.Matrix([[S.Rational(x.numerator,x.denominator) if isinstance(x,F) else S.Integer(x) for x in row] for row in vs]).rank()


checks=0
for p in range(2,7):
    for q in range(2,7):
        n=p+q;h=max(p,q);lo=min(p,q);eps=h%2
        ns=normals(p,q)
        vs=roots(p,q)
        assert len(ns)==2**p+2**q-2
        checks += 1
        # All asserted normals are genuine supporting hyperplanes with
        # dimension n-2, and all root points obey their inequalities.
        if n<=9:
            for z in ns:
                dots=[dot(z,v) for v in vs]
                assert max(dots)==1
                face=[v for v,b in zip(vs,dots) if b==1]
                base=face[0]
                assert rank([[a-b for a,b in zip(v,base)] for v in face[1:]])==n-2
                checks +=2
        norm2={z:dot(z,z) for z in ns}
        maxval=F(h,1)-F(eps,n)
        assert max(norm2.values())==maxval
        checks+=1
        active=[z for z in ns if norm2[z]==maxval]
        expected=comb(h,h//2) if h%2==0 else 2*comb(h,(h-1)//2)
        if p==q:expected*=2
        assert len(active)==expected
        checks+=1
        rnk=rank(active)
        dimension=n-1-rnk
        if p==q:want=1 if p%2==0 else 0
        else:want=lo if h%2==0 else lo-1
        assert dimension==want,(p,q,dimension,want)
        checks+=1
        # Normal tightness is antipodally symmetric; every feasible center
        # must annihilate the span of all active normals.
        assert set(active)==set(tuple(-x for x in z) for z in active)
        checks+=1

# Exact even-balanced endpoint inequality, checking all sign sums (not
# replacing the monotonicity proof for unbounded m).
for m in range(2,14,2):
    f=lambda s:(1-S.sqrt(1-S.Rational(s*s,2*m*m)))/s
    for s in range(2,m+1,2):
        assert S.simplify(f(s)-f(2)).is_nonnegative is True
        checks+=1
print('PASS:', checks, 'exact rational checks over 25 bipartition pairs plus six balanced cases')
