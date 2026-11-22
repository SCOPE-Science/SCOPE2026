#!/usr/bin/env python3
"""Independent exact-arithmetic diagnostics for a trivariate copula tail theorem.

The finite dyadic enumeration is diagnostic, not the proof of the
continuous-threshold statements established analytically in RESULT.md.
"""
from fractions import Fraction as F


def envelope(t):
    p = 1-t
    return min(p*p, 1-3*p+3*p*p)


def parity_tail(t):
    p = 1-t
    if p >= F(1, 2):
        return 1 - 3*t + 3*t*t
    if p == 0:
        return F(0)
    k = 1
    while p < F(1, 2**(k+1)):
        k += 1
    return F(1, 4**k) - 3*F(1, 2**k)*p + 3*p*p


def dyadic_gap(t):
    p = 1-t
    if p >= F(1, 2) or p == 0:
        return F(0)
    k = 1
    while p < F(1, 2**(k+1)):
        k += 1
    return 2*(p-F(1, 2**(k+1)))*(F(1, 2**k)-p)


def bernoulli_table(p):
    r = envelope(1-p)
    out = {}
    for a in range(2):
        for b in range(2):
            for c in range(2):
                count = a+b+c
                out[(a,b,c)] = (r if count == 3 else
                      p*p-r if count == 2 else
                      p-2*p*p+r if count == 1 else
                      1-3*p+3*p*p-r)
    return out


def verify():
    checks = 0
    for m in range(1, 7):
        N = 2**m
        for j in range(N+1):
            t = F(j, N)
            count = sum(
                (i >= j and k >= j and (N-1-(i^k)) >= j)
                for i in range(N) for k in range(N)
            )
            actual = F(count, N*N)
            assert actual == parity_tail(t), (m, j, actual, parity_tail(t))
            checks += 1
            assert envelope(t)-actual == dyadic_gap(t), (m, j)
            checks += 1
            assert F(0) <= actual <= envelope(t), (m,j)
            checks += 1
            p = 1-t
            T = bernoulli_table(p)
            assert sum(T.values(), F(0)) == 1 and all(v >= 0 for v in T.values())
            checks += 1
            for i in range(3):
                assert sum(v for key,v in T.items() if key[i]==1) == p
                checks += 1
            for i,k in ((0,1),(0,2),(1,2)):
                assert sum(v for key,v in T.items() if key[i]==1 and key[k]==1) == p*p
                checks += 1
            assert T[(1,1,1)] == envelope(t)
            checks += 1
    # Sharp relative ratio on each dyadic scale (not merely sampled values).
    for k in range(1, 17):
        p = F(2,3)*F(1,2**k)
        t = 1-p
        assert parity_tail(t)*4 == envelope(t)*3
        checks += 1
        # Each scale has zeros at both dyadic endpoints.
        for q in (F(1,2**k), F(1,2**(k+1))):
            assert parity_tail(1-q) == q*q
            checks += 1
    assert envelope(F(5,8)) == F(9,64)
    assert parity_tail(F(5,8)) == F(7,64)
    assert dyadic_gap(F(5,8)) == F(1,32)
    assert F(1,32) - F(12,512) == F(1,128)
    checks += 4
    print(f"PASS {checks} exact rational checks; all dyadic grid probabilities checked for m<=6")

if __name__ == '__main__':
    verify()
