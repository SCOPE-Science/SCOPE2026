"""Exact rational finite-word consistency checks for cyclic mechanical codings.

These finite checks illustrate the separate analytic irrational-rotation theorem;
they do not certify any irrational limiting statement.
"""
from fractions import Fraction
from math import ceil, floor, gcd

checks = 0
for p, q in [(89,144), (71,171)]:
    alpha = Fraction(p,q)
    assert gcd(p,q) == 1
    for k in (3,4,5,7):
        assert gcd(p,k) == 1
        # Avoid the rational cutting points (positive shift epsilon).
        epsilon = Fraction(1, 10*q)
        N = k*q
        u = [int((epsilon + Fraction(j*p,q)) // 1) % k for j in range(N+16)]
        for n in range(1, min(15,q)+1):
            factors = {tuple(u[i:i+n]) for i in range(N)}
            pal = {w for w in factors if w == w[::-1]}
            assert len(factors) == k*n, (p,q,k,n,len(factors),k*n)
            checks+=1
            expected = k if (n-1)*p < q else 0
            assert len(pal) == expected, (p,q,k,n,len(pal),expected)
            checks+=1
            assert all(len(set(w)) == 1 for w in pal)
            checks+=1
            for w in factors:
                assert all((w[i+1]-w[i]) % k in (0,1) for i in range(len(w)-1))
                checks+=1
print('FINITE_RATIONAL_CHECKS_PASS',checks)
