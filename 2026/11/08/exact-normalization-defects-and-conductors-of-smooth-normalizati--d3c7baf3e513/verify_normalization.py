#!/usr/bin/env python3
"""Exact finite checks for normalization-defect and conductor formulas.

Run with Python >=3.9. This performs finite tests only; the general claims
require the accompanying mathematical proof.
"""
from itertools import product
from math import comb, gcd, prod


def numerical_semigroup(n, m, bound):
    return {i*n + j*m for i in range(bound//n + 1)
            for j in range(bound//m + 1) if i*n + j*m <= bound}


def distance(b, H):
    return b - max(z for z in H if z <= b)


def direct_exponent(a, b, n, m, lam):
    # Independent coefficient generator check, not a restatement of the
    # closed numerical-semigroup formula.
    for counts in product(*(range(ai//li + 1) for ai, li in zip(a,lam))):
        rem = b - sum(counts)
        if rem < 0:
            continue
        for j in range(rem//m + 1):
            if (rem-j*m) % n == 0:
                return True
    return False


def check(n, m, lam):
    s = len(lam)+1
    c = (n-1)*(m-1)
    H = numerical_semigroup(n,m,c+10)
    q = [distance(b,H) for b in range(c+3)]
    assert q[c:] == [0,0,0]
    Q = [max(q[b:]) for b in range(c+1)]
    assert Q[0] == n-1 and Q[c] == 0
    predicted = prod(lam)*sum(comb(v+s-2,s-1) for v in q[:c] if v)
    observed = 0
    low_caps = [li*n for li in lam]
    for b in range(c+1):
        for a in product(*(range(L) for L in low_caps)):
            capacity = sum(ai//li for ai,li in zip(a,lam))
            actual = direct_exponent(a,b,n,m,lam)
            assert actual == (capacity >= q[b]), (n,m,lam,a,b,capacity,q[b])
            if not actual:
                observed += 1
            conductor = capacity >= Q[b]
            future_in_R = all(direct_exponent(a,b+t,n,m,lam)
                              for t in range(c+1-b))
            assert future_in_R == conductor, (n,m,lam,a,b,Q[b])
    assert predicted == observed, (n,m,lam,predicted,observed)
    if m == n+1:
        assert predicted == prod(lam)*comb(n+s-1,s+1)
    return 1


def main():
    cases=0
    for n in range(2,8):
        for m in range(n+1,min(n+7,14)):
            if gcd(n,m)!=1:
                continue
            for lam in ((1,),(2,),(1,1),(1,2),(2,2),(1,1,1)):
                cases += check(n,m,lam)
    print('NORMALIZATION_DEFECT_AND_CONDUCTOR_FINITE_CHECK_OK',cases)

if __name__=='__main__':
    main()
