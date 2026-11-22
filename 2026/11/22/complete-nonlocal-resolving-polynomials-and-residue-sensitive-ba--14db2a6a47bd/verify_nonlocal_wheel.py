#!/usr/bin/env python3
"""Exact integer checks for resolving-set enumerators of labelled wheel graphs.

No external packages required. This finite test supports, but does not replace,
the unrestricted cyclic-gap proof.
"""
from collections import Counter
from math import comb
from fractions import Fraction


def choose(a, b):
    return comb(a, b) if isinstance(a, int) and 0 <= b <= a else 0


def gap_ok(n, mask, ordinary=False):
    vertices = [v for v in range(n) if mask & (1 << v)]
    if len(vertices) < 2:
        return False
    gaps = [(vertices[(j+1) % len(vertices)] - vertices[j] - 1) % n
            for j in range(len(vertices))]
    if max(gaps) > (3 if ordinary else 4):
        return False
    if sum(g >= 3 for g in gaps) > 1:
        return False
    return all(gaps[(j-1) % len(gaps)] <= 1 and
               gaps[(j+1) % len(gaps)] <= 1
               for j, g in enumerate(gaps) if g >= 2)


def direct_wheel(n, rim_mask, with_hub=False, ordinary=False):
    # The graph has labelled rim 0,...,n-1 and hub n.
    selected = [v for v in range(n) if rim_mask & (1 << v)]
    if with_hub:
        selected.append(n)
    def dist(a, b):
        if a == b:
            return 0
        if a == n or b == n:
            return 1
        return 1 if (a - b) % n in (1, n-1) else 2
    for a in range(n+1):
        for b in range(a+1, n+1):
            if not ordinary and (a == n or b == n or (a-b) % n in (1, n-1)):
                continue
            if all(dist(a, s) == dist(b, s) for s in selected):
                return False
    return True


def exact_gap_coefficient(n, k):
    no_long = 0
    for j in range(k//2+1):
        c = choose(k-j, j)*choose(k-j, n-k-2*j)
        if c:
            no_long += Fraction(n*c, k-j)
    one_long = 0
    for e in (3, 4):
        for j in range(k//2+1):
            one_long += n*choose(k-2-j, j)*choose(k-1-j, n-k-e-2*j)
    assert no_long.denominator == 1
    return int(no_long)+one_long


def basis_formula(n):
    s, r = divmod(n, 5)
    if r == 0:
        return 5*(s+1)*(s**4+9*s**3+14*s**2-24*s+24)//24
    if r == 1:
        return (5*s+1)*(s*s+s+2)//2
    if r == 2:
        return 5*s+2
    if r == 3:
        return s*(5*s+3)*(s*s+6*s+11)//6
    return s*(5*s+4)


def coefficient_by_rational_series(max_n):
    # D=1-z*x-z*x^2-z^2*x^4-z^2*x^5.
    h = [Counter() for _ in range(max_n+1)]
    h[0][0] = 1
    for n in range(1, max_n+1):
        for shift, weight_degree in ((1,1),(2,1),(4,2),(5,2)):
            if n >= shift:
                for k,v in h[n-shift].items():
                    h[n][k+weight_degree] += v
    out = {}
    for n in range(7, max_n+1):
        poly = Counter()
        for shift, kd, scalar in ((1,1,1),(2,1,2),(4,2,4),(5,2,5),
                                  (5,2,n),(6,2,2*n),(7,2,n)):
            if n >= shift:
                for k,v in h[n-shift].items():
                    poly[k+kd] += scalar*v
        out[n] = poly
    return out


def main():
    polys = coefficient_by_rational_series(220)
    tests = 0
    for n in range(7, 17):
        nl = Counter()
        metric = Counter()
        for mask in range(1 << n):
            a = direct_wheel(n, mask, False, False)
            b = direct_wheel(n, mask, True, False)
            c = direct_wheel(n, mask, False, True)
            d = direct_wheel(n, mask, True, True)
            assert a == b, (n,mask,'hub nonlocal')
            assert c == d, (n,mask,'hub ordinary')
            assert a == gap_ok(n, mask), (n,mask,'gap nonlocal')
            assert c == gap_ok(n, mask, True), (n,mask,'gap ordinary')
            if a: nl[mask.bit_count()] += 1
            if c: metric[mask.bit_count()] += 1
            tests += 1
        assert nl == polys[n], (n, 'rational coefficient',nl,polys[n])
        assert all(nl[k] == exact_gap_coefficient(n,k) for k in range(n+1))
        assert nl[min(nl)] == basis_formula(n)
        assert min(nl) == 2*n//5
        print('n',n,'nonlocal_rim',sum(nl.values()),
              'ordinary_rim',sum(metric.values()),
              'nonlocal_bases',nl[min(nl)],'minimum',min(nl))
    for n in range(17,221):
        k=2*n//5
        assert polys[n][k] == exact_gap_coefficient(n,k) == basis_formula(n), n
        assert not any(polys[n][j] for j in range(k))
        assert polys[n][n] == 1
    print('EXHAUSTIVE_RIM_MASKS',tests)
    print('RATIONAL_AND_BINOMIAL_BASE_VALUES_TO_220_OK')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
