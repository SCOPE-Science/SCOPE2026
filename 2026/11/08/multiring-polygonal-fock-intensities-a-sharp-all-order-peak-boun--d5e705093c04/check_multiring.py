"""Exact rational spot certificates for the concentric polygon peak construction.

The all-order theorem uses analytic Descartes and exponential estimates;
this finite checker verifies selected integer instances, not the universal theorem.
"""
from fractions import Fraction
from math import ceil, log


def poly_coeffs(a):
    c = [1]
    for x in a:
        nxt = [0] * (len(c) + 1)
        for j, q in enumerate(c):
            nxt[j] += x * q
            nxt[j + 1] += q
        c = nxt
    return c


def verify(k):
    n = 4 * ceil(8 * k * log(8*k) / 4)
    assert n >= 3 and n >= 8 * k * log(8*k)
    m = n // 2
    # c_j=j-1/2; a_j=(n*c_j)^(n/2) exact integer when n is even.
    a = [(n * (2*j-1) // 2) ** m for j in range(1, k+1)]
    C = poly_coeffs(a)
    assert len(C) == k+1 and all(v > 0 for v in C)
    # P(r)=Q(r^n)-n*r^(n-2)*Q'(r^n)
    terms = {}
    for j, q in enumerate(C):
        terms[n*j] = terms.get(n*j, 0) + q
        if j:
            terms[n*j-2] = terms.get(n*j-2, 0) - n*j*q
    exponents = sorted(terms)
    signs = [1 if terms[x]>0 else -1 for x in exponents]
    assert all(v != 0 for v in terms.values())
    assert sum(signs[i]!=signs[i-1] for i in range(1,len(signs))) == 2*k
    assert len(terms) == 2*k+1
    # Evaluate S(x)-x exactly at the 2k+1 prescribed quarter-integer nodes.
    def value(num):
        # x=num/4, n*x integer because n multiple of four.
        x = Fraction(num,4)
        t = ((n*num)//4) ** m
        S = sum((Fraction(t,t+ai) for ai in a), Fraction(0))
        return S-x
    signs_at_nodes = []
    for j in range(1,k+1):
        v_before = value(4*j-3) # j-3/4
        v_after = value(4*j-1) # j-1/4
        assert v_before < 0 and v_after > 0
        signs_at_nodes.extend(['-', '+'])
    assert value(4*k+1) < 0
    # 2k disjoint sign-change intervals, and at most 2k roots
    # counted with multiplicity by Descartes: exactly 2k simple positive roots.
    return n, 2*k, k*n+1, len(str(max(a)))

for k in range(1,7):
    n, roots, peaks, digits = verify(k)
    print(f'k={k} n={n} radial_simple_roots={roots} total_nondegenerate_peaks={peaks} parameter_digits={digits}')
print('MULTIRING_POLYGON_PEAK_CHECK_PASS')
