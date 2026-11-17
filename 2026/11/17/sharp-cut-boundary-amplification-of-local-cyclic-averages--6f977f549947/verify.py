#!/usr/bin/env python3
"""Exact rational checks for finite cyclic averaging in open-path variation.

Run with Python 3.9+; standard library only. These finite diagnostics support,
but do not replace, the all-dimension mathematical proof.
"""
from fractions import Fraction as F
from math import comb
from itertools import product


def apply(n, probs, x):
    return [sum((probs[s] * x[(i+s) % n] for s in range(n)), F(0))
            for i in range(n)]


def var(x):
    return sum((abs(x[i+1]-x[i]) for i in range(len(x)-1)), F(0))


def sharp_by_steps(n, probs):
    return max(var(apply(n, probs, [F(int(i < k)) for i in range(n)]))
               for k in range(1, n))


def uniform(n, m):
    return [F(int(s<m),m) for s in range(n)]


def c_uniform(n, m):
    return F(2*m-1,m) if 2*m <= n else F(2*(n-m),m)


def binomial(n, r):
    p=[F(0) for _ in range(n)]
    for s in range(r+1):
        p[s % n] += F(comb(r,s),2**r)
    return p


def test_all():
    # Exact n,m phase diagram, including m=1 and m=n.
    total=0
    for n in range(2,31):
        for m in range(1,n+1):
            p=uniform(n,m)
            found=sharp_by_steps(n,p)
            expected=c_uniform(n,m)
            assert found == expected, (n,m,found,expected)
            total+=1
    print('EXACT_UNIFORM_ALL_N2_TO_N30_ALL_WINDOWS_PASS',total)

    # General support theorem, testing zero and unbalanced probabilities.
    total=0
    for n in range(2,15):
        for m in range(1,n//2+1):
            for coeff in product(range(3), repeat=m):
                if not any(coeff):
                    continue
                denom=sum(coeff)
                p=[F(v,denom) for v in coeff]+[F(0)]*(n-m)
                found=sharp_by_steps(n,p)
                expected=2-p[0]
                assert found==expected,(n,m,coeff,found,expected)
                total+=1
    print('EXACT_LOCAL_SUPPORT_MASS_LAW_PASS',total)

    # All early powers of two-tap averaging.
    total=0
    for n in range(2,40):
        for r in range((n-2)//2+1):
            c=sharp_by_steps(n,binomial(n,r))
            assert c==2-F(1,2**r),(n,r,c)
            total+=1
    print('EXACT_BINOMIAL_INITIAL_TRANSIENT_PASS',total)

    # Direct exact arbitrary-signal checks, not merely steps.
    total=0
    for n in range(2,8):
        for m in range(1,n+1):
            p=uniform(n,m)
            C=c_uniform(n,m)
            for data in product((-1,0,1), repeat=n):
                x=[F(v) for v in data]
                assert var(apply(n,p,x))<=C*var(x)
                total+=1
    print('EXACT_DIRECT_TERNARY_INPUTS_PASS',total)

    # Fixed n long-time gradient norm tends to zero; sampled exact powers.
    for n in range(3,11):
        p=binomial(n,80)
        assert sharp_by_steps(n,p) < F(1,4),n
    print('LONG_TIME_EXACT_FINITE_SANITY_PASS')
    print('ALL_CYCLIC_OPEN_PATH_VARIATION_CHECKS_PASS')

if __name__=='__main__':
    test_all()
