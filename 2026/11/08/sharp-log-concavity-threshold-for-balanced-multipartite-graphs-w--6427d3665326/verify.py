#!/usr/bin/env python3
"""Exact integer/rational verification of the five-vertex-part general-position theorem.

Run: python3 verify.py
Standard library only. The symbolic identities are checked as polynomial identities,
not by evaluating at finitely many parameter values. Finite graph enumeration is separate.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb, factorial


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(p, q):
    return trim([(p[i] if i < len(p) else 0) +
                 (q[i] if i < len(q) else 0) for i in range(max(len(p), len(q)))])


def mul(p, q):
    out = [Q(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a*b
    return trim(out)


def scale(p, a):
    return trim([a*x for x in p])


def choose_var(k):
    p = [Q(1)]
    for i in range(k):
        p = mul(p, [Q(-i), Q(1)])
    return scale(p, Q(1, factorial(k)))


def shift(p, c):
    """Coefficients of p(u+c), ascending in u."""
    out = [Q(0)]
    for a in reversed(p):
        out = add(mul(out, [Q(c), Q(1)]), [a])
    return out


def difference(a, k):
    return add(mul(a[k], a[k]), scale(mul(a[k-1], a[k+1]), -1))


CERTIFICATES = {
    2: (4, Q(25,12), [759,320,25]),
    3: (4, Q(25,144), [60858,72015,31525,6625,625]),
    4: (4, Q(5,576), [2979828,8200500,8925725,5037500,1563750,250000,15625]),
    5: (4, Q(1,3456), [3456,73642500,275730000,427720625,354945625,
                       169156250,46093750,6640625,390625]),
    6: (6, Q(15625,145152), [63000000,233682720,372068044,337220100,
                               193569635,73775340,18954231,3247500,
                               355625,22500,625]),
}


def verify_symbolic():
    t = [Q(0), Q(1)]
    a = [[Q(1)], scale(t, Q(5))]
    for k in range(2, 8):
        a.append(add(scale(choose_var(k), Q(5**k)),
                     scale(t, Q(comb(5,k) if k <= 5 else 0))))
    assert difference(a, 1) == [Q(0), Q(5,2), Q(25,2)]
    for k, (base, multiplier, expected) in CERTIFICATES.items():
        d = difference(a, k)
        assert d[:2] == [0, 0], (k, d[:2])
        p = shift(d[2:], base)
        assert p == scale(expected, multiplier), (k, p)
        assert all(x > 0 for x in expected), k
    print('SYMBOLIC_ALL_PARAMETERS_POSITIVE_COEFFICIENT_CERTIFICATES_OK')


def coefficients(t):
    return [1,5*t] + [5**k*comb(t,k) + t*comb(5,k)
                        for k in range(2,max(5,t)+1)]


def verify_transitions():
    a2, a3 = coefficients(2), coefficients(3)
    assert a2 == [1,10,45,20,10,2]
    assert a3 == [1,15,105,155,15,3]
    assert a2[3]**2-a2[2]*a2[4] == -50
    assert a3[4]**2-a3[3]*a3[5] == -240
    for t in range(4,201):
        a = coefficients(t)
        assert all(a[k]**2 > a[k-1]*a[k+1] for k in range(1,len(a)-1)),t
    print('SHARP_FAILURES_AND_SAMPLE_PARAMETERS_OK')


def graph_enumeration(t):
    n=5*t
    dist = [[0 if u==v else (2 if u//5==v//5 else 1)
             for v in range(n)] for u in range(n)]
    counts = [0]*(n+1)
    for mask in range(1<<n):
        vertices=[i for i in range(n) if (mask>>i)&1]
        valid=True
        for i,j,k in combinations(vertices,3):
            if (dist[i][j]+dist[j][k]==dist[i][k] or
                dist[i][k]+dist[k][j]==dist[i][j] or
                dist[j][i]+dist[i][k]==dist[j][k]):
                valid=False
                break
        if valid:
            counts[len(vertices)]+=1
    expected=coefficients(t)
    assert counts[:len(expected)]==expected,(t,counts,expected)
    assert not any(counts[len(expected):])
    print('INDEPENDENT_GEODESIC_ENUMERATION_OK',t,'vertices',n,'sets',sum(counts))


if __name__=='__main__':
    verify_symbolic()
    verify_transitions()
    for t in (2,3):
        graph_enumeration(t)
    print('VERIFY_OK')
