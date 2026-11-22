#!/usr/bin/env python3
"""Exact checks of magnetic flower tight-binding spectral inverse formula."""
import sympy as S
from collections import defaultdict
from functools import reduce
z=S.Symbol('z')
I=S.I

def matrix(ts,us):
    m=len(ts)
    H=S.zeros(2*m+1)
    for j,(t,u) in enumerate(zip(ts,us)):
        a=2*j+1; b=a+1
        H[0,a]=H[a,0]=H[0,b]=H[b,0]=1
        H[a,b]=S.sympify(t)*u
        H[b,a]=S.sympify(t)*S.conjugate(u)
    return H

def predicted(ts,us):
    pr=S.prod(z*z-S.sympify(t)**2 for t in ts)
    return S.Poly(S.expand(z*pr-S.Add(*[(2*z+S.sympify(t)*(u+S.conjugate(u)))*S.prod(z*z-S.sympify(t2)**2 for k,t2 in enumerate(ts) if k!=j) for j,(t,u) in enumerate(zip(ts,us))])),z)

def recover(ts,polynomial):
    groups=defaultdict(list)
    for j,t in enumerate(ts):groups[S.sympify(t)].append(j)
    distinct=sorted(groups)
    divisor=S.prod((z*z-t*t)**(len(groups[t])-1) for t in distinct)
    q=S.Poly(S.cancel(polynomial.as_expr()/divisor),z)
    cs={}
    for t in distinct:
        d=S.prod(t*t-v*v for v in distinct if v!=t)
        cs[t]=S.cancel(-q.eval(t)/(2*t*d)-len(groups[t]))
    return cs

cases=[
 ([1,1],[S.Rational(3,5)+S.Rational(4,5)*I,S.Rational(5,13)+S.Rational(12,13)*I]),
 ([1,2,3],[1,-1,S.Rational(3,5)+S.Rational(4,5)*I]),
 ([1,1,2],[S.Rational(3,5)+S.Rational(4,5)*I,S.Rational(3,5)-S.Rational(4,5)*I,S.Rational(5,13)+S.Rational(12,13)*I]),
 ([1,2,2,3],[1,S.Rational(3,5)+S.Rational(4,5)*I,-1,S.Rational(5,13)+S.Rational(12,13)*I]),
 ([2,2,2,2],[-1,-1,-1,-1]),
 ([1,1,2,2],[1,-1,1,-1]),
]
for ts,us in cases:
    h=matrix(ts,us)
    actual=h.charpoly(z).as_poly(z)
    target=predicted(ts,us)
    assert S.expand(actual.as_expr()-target.as_expr())==0,(ts,us,actual-target)
    rec=recover(ts,actual)
    for t,C in rec.items():
        expected=S.expand(sum((u+S.conjugate(u))/2 for k,u in enumerate(us) if ts[k]==t))
        assert S.simplify(C-expected)==0,(ts,t,C,expected)
    for j,(t,u) in enumerate(zip(ts,us)):
        moment=S.simplify((h**3)[2*j+1,2*j+1]); expected=S.expand(t*(u+S.conjugate(u)))
        assert moment==expected,(ts,j,moment,expected)
    print('PASS exact:',ts,'degree',actual.degree(),'groups', {str(k):str(v) for k,v in rec.items()},'moment checks',len(ts))

# Non-gauge-equivalent, equal-magnitude-weight configurations can be globally isospectral.
# cosines [3/5,-3/5] and [0,0] have matching sums but different local moments.
u1=S.Rational(3,5)+S.Rational(4,5)*I
u2=-S.Rational(3,5)+S.Rational(4,5)*I
v1=I;v2=-I
h1=matrix([1,1],[u1,u2]);h2=matrix([1,1],[v1,v2])
assert h1.charpoly(z).as_expr()==h2.charpoly(z).as_expr()
assert S.simplify((h1**3)[1,1]-(h2**3)[1,1])==S.Rational(6,5)
print('PASS isospectral-but-local-distinct example (difference 6/5)')

# Breaking coupling degeneracy recovers individual cosines from spectral data.
h1=matrix([1,2],[u1,u2]);h2=matrix([1,2],[v1,v2]);assert h1.charpoly(z)!=h2.charpoly(z)
print('PASS distinct-link spectral identifiability')
print('ALL CHECKS PASSED')
