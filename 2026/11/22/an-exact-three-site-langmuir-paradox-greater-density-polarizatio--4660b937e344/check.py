#!/usr/bin/env python3
"""Exact algebra and independent finite-state checks for a three-site exclusion--exchange chain.

Run: python check.py
Requires only Python's standard library.
"""
from fractions import Fraction as F


class P:
    """Bivariate polynomial over rationals; indices are powers of (a,w)."""
    def __init__(self, terms=None):
        self.t = {k: F(v) for k, v in (terms or {}).items() if v}

    @staticmethod
    def cv(z):
        return z if isinstance(z, P) else P({(0, 0): F(z)})

    def __add__(self, other):
        d = self.t.copy()
        for k, v in P.cv(other).t.items():
            d[k] = d.get(k, F(0)) + v
        return P(d)
    __radd__ = __add__

    def __neg__(self):
        return P({k: -v for k, v in self.t.items()})

    def __sub__(self, other):
        return self + -P.cv(other)

    def __rsub__(self, other):
        return P.cv(other) - self

    def __mul__(self, other):
        d = {}
        for (i,j), c in self.t.items():
            for (k,l), v in P.cv(other).t.items():
                z = (i+k,j+l)
                d[z] = d.get(z, F(0)) + c*v
        return P(d)
    __rmul__ = __mul__

    def __pow__(self, n):
        assert isinstance(n,int) and n>=0
        r = P.cv(1)
        for _ in range(n): r=r*self
        return r

    def __eq__(self, other):
        return self.t == P.cv(other).t

    def diff_w(self):
        return P({(i,j-1):j*c for (i,j),c in self.t.items() if j})

    def eval(self, aa,ww):
        return sum((c*(aa**i)*(ww**j) for (i,j),c in self.t.items()),F(0))


a=P({(1,0):1}); w=P({(0,1):1}); one=P.cv(1)
D=2*a**3+4*a**2*w+3*a**2+4*a*w+2*a+w
B=(2*a+1)**2
h=[a*(2*w+1), a*a*(2*a+4*w+1), 2*a*(a+w),
   a*a*(2*a+4*w+1), a+w, 2*a*(a+w), a+w, a*(2*w+1)]
assert sum(h,P.cv(0)) == 2*D


def transitions(s):
    """(next state, exact rate polynomial); site 1 is the lowest bit."""
    out=[]
    if not s&1: out.append((s|1,a))
    if s&4: out.append((s&~4,a))
    for j in range(2):
        if (s>>j)&1 and not (s>>(j+1))&1:
            out.append((s^(3<<j),one))
    if (s>>1)&1:out.append((s&~2,w))
    else:out.append((s|2,w))
    return out

balance=[P.cv(0) for _ in range(8)]
for s in range(8):
    for t,rate in transitions(s):
        balance[t]=balance[t]+rate*h[s]
        balance[s]=balance[s]-rate*h[s]
assert all(z==0 for z in balance), 'stationary master equation failed'

M=[sum((h[s] for s in range(8) if s>>j&1),P.cv(0)) for j in range(3)]
Joint={(i,j):sum((h[s] for s in range(8) if s>>i&1 and s>>j&1),P.cv(0))
       for i,j in [(0,1),(1,2),(0,2)]}
assert M[0] == a*(2*a+1)*(2*a+4*w+1)
assert M[1] == D
assert M[2] == 2*a*a+4*a*w+3*a+2*w
for i,j in [(0,1),(1,2)]:
    assert (2*D*Joint[i,j] - M[i]*M[j]) == a*(1-2*a)*D
assert 2*D*Joint[0,2]-M[0]*M[2] == a*a*(1-2*a)*(2*a+4*w+1)

H=a*a+2*a*w+a+w
assert M[2]-M[0] == 2*(1-2*a)*H
assert D.diff_w()==B
assert H.diff_w()*D-H*D.diff_w()==a*(2*a+1)
N=a*a*(1-2*a)*(2*a+4*w+1)
assert N.diff_w()*D-2*N*D.diff_w() == 2*a*a*(2*a-1)*(2*D-2*a+1)


def independent_stationary(aa,ww):
    """Rational Gauss-Jordan solve, not using candidate stationary weights."""
    q=[[F(0) for _ in range(8)] for _ in range(8)]
    for s in range(8):
        for t,rate in transitions(s):
            r=rate.eval(aa,ww)
            q[t][s]+=r
            q[s][s]-=r
    q[7]=[F(1)]*8
    aug=[row+[F(i==7)] for i,row in enumerate(q)]
    for k in range(8):
        piv=next(i for i in range(k,8) if aug[i][k])
        aug[k],aug[piv]=aug[piv],aug[k]
        z=aug[k][k]
        aug[k]=[v/z for v in aug[k]]
        for i in range(8):
            if i!=k:
                mul=aug[i][k]
                aug[i]=[x-mul*y for x,y in zip(aug[i],aug[k])]
    return [row[-1] for row in aug]

checks=0
for aa in [F(1,10),F(2,5),F(1,2),F(4,5),F(2,1)]:
    for ww in [F(0),F(1,10),F(1),F(13)]:
        p=independent_stationary(aa,ww)
        den=2*D.eval(aa,ww)
        assert p == [u.eval(aa,ww)/den for u in h]
        checks+=1
print('PASS: 8 polynomial balance laws, normalization, mean and covariance identities,')
print('derivative sign identities, and',checks,'independent exact-rational stationary solves.')
