#!/usr/bin/env python3
"""Exact polynomial checks for seed-dependent percolation on complete bipartite graphs."""
from itertools import product
import sympy as S
p,z,t=S.symbols('p z t');q=1-p;c=1-q*q

def high(b):
    return z*q**b*(1+p*z)**b+z*z*((q*q+c*z)**b-(q*q+2*p*q*z)**b)
def low(b):
    return q*q*z+2*p*q*z*high(b-1)+p*p*z**3*(q*q+c*z)**(b-1)
def mean(f):return S.expand(S.diff(f,z).subs(z,1))
def variance(f):
    m=mean(f)
    return S.factor(S.diff(f,z,2).subs(z,1)+m-m*m)
def enumerated(b, high_root):
    edges=[(i,2+j) for i in (0,1) for j in range(b)]
    out=0
    for mask in range(1<<(2*b)):
        par=list(range(b+2))
        def root(i):
            while par[i]!=i:i=par[i]
            return i
        for k,(i,j) in enumerate(edges):
            if mask>>k&1:par[root(i)]=root(j)
        v=0 if high_root else 2
        size=sum(root(w)==root(v) for w in range(b+2))
        m=mask.bit_count()
        out+=z**size*p**m*q**(2*b-m)
    return S.Poly(out,z,p)

for b in (2,3,4):
    assert S.Poly(S.expand(high(b)),z,p)==enumerated(b,True)
    assert S.Poly(S.expand(low(b)),z,p)==enumerated(b,False)
print('PGF_EXHAUSTIVE_OK: 16+64+256 edge configurations per each of two seed types')

F=20*p**9-56*p**8+7*p**7+56*p**6+8*p**5-10*p**4-42*p**3+3*p**2-2*p+1
D=S.factor(variance(high(3))-variance(low(3)))
M=S.factor(mean(high(3))-mean(low(3)))
assert S.expand(D-p*q*q*F)==0
assert S.expand(M-p*q*q*(1+p+3*p*p-2*p**3))==0
Q=S.Poly(S.cancel((1+t)**9*F.subs(p,t/(1+t))),t)
expected=[1,7,23,7,-185,-581,-775,-464,-130,-15]
assert [Q.nth(i) for i in range(10)]==expected
assert Q.nth(0)>0 and Q.nth(9)<0
assert (F.subs(p,S.Rational(25155,100000))>0 and F.subs(p,S.Rational(25156,100000))<0)
assert variance(high(3)).subs(p,S.Rational(1,2))==S.Rational(2007,1024)
assert variance(low(3)).subs(p,S.Rational(1,2))==S.Rational(2535,1024)
print('K23_UNIQUE_CROSSING_AND_MEAN_OK: root in (0.25155,0.25156); at p=1/2 delta -33/64')
for b in (3,4,5):
    d=S.factor(variance(high(b))-variance(low(b)))
    assert S.diff(d,p).subs(p,0)==b-2
    assert S.limit(d/q**2,p,1)==-b*(b+2)
print('FINITE_ENDPOINT_POLYNOMIAL_CHECKS_OK: b=3..5; general b endpoint proof is combinatorial')
print('VERIFY_OK')
