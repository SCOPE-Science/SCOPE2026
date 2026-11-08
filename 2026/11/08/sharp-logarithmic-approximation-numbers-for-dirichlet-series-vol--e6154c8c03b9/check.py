#!/usr/bin/env python3
"""Finite standalone checks of the Dirichlet-Volterra coefficient and prime-block formulas.
Python standard library only. Finite checks do not establish the asymptotic theorem.
"""
from math import log, gcd, sqrt, isclose
from collections import defaultdict


def direct_column(n, g):
    return {n * m: b * log(m) / log(n * m) for m, b in g.items() if m > 1 and b}


def derived_column(n, g):
    d = defaultdict(float)
    for m, b in g.items():
        if m > 1:
            d[n*m] += b * log(m)
    return {k: v / log(k) for k,v in d.items() if v}


def apply_b(vec, g):
    out = defaultdict(float)
    for n, c in vec.items():
        for m, b in g.items():
            if m > 1: out[n*m] += c*b*log(m)
    return out


def apply_t(vec, g):
    return {k:v/log(k) for k,v in apply_b(vec,g).items()}


def norm(vec):
    return sqrt(sum(abs(v)**2 for v in vec.values()))


def prime_block_h(base, degree):
    # tensor of normalized initial geometric polynomials in primes 2 and 3
    c = 1.0/(degree+1)
    return {base*(2**i)*(3**j):c for i in range(degree+1) for j in range(degree+1)}


def check():
    g={2:1.0,3:1.0}
    count=0
    for n in range(1,101):
        a,b=direct_column(n,g),derived_column(n,g)
        assert set(a)==set(b)
        for k in a:
            assert isclose(a[k],b[k],rel_tol=1e-14,abs_tol=1e-14)
            count+=1
    # Exact single-prime singular-value sequence: columns have disjoint supports.
    q=5; coef=2.0
    cols=[direct_column(n,{q:coef}) for n in range(1,101)]
    assert len(set.union(*[set(v) for v in cols]))==100
    values=[norm(v) for v in cols]
    for n,x in enumerate(values,1):
        assert isclose(x,abs(coef)*log(q)/log(q*n),rel_tol=1e-14)
        count+=1
    # Distinct coprime bases define orthogonal input and output blocks.
    for degree in [1,3,8,24,50]:
        h1=prime_block_h(35,degree)
        h2=prime_block_h(55,degree)
        assert isclose(norm(h1),1,rel_tol=1e-12)
        assert not (set(h1)&set(h2))
        Bh1,Bh2=apply_b(h1,g),apply_b(h2,g)
        assert not(set(Bh1)&set(Bh2))
        ratio=norm(Bh1)/(log(2)+log(3))
        assert 0.5<ratio<=1+1e-12
        count+=4
    # Slow denominator: ratio approaches fixed polynomial-block B norm.
    h=prime_block_h(1,8)
    Bnorm=norm(apply_b(h,g))
    for k in [8,12,18]:
        m=5*(10**k)+7 # relatively prime to 6
        while gcd(m,6)!=1: m+=1
        hm=prime_block_h(m,8)
        value=log(m)*norm(apply_t(hm,g))
        assert abs(value-Bnorm)<2.0*Bnorm*log(100000)/log(m)
        count+=1
    print('DIRICHLET_VOLTERRA_CHECK_OK',count,'finite checks')

if __name__=='__main__': check()
