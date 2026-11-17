#!/usr/bin/env python3
"""Reproduce exact facet-measure identities and independent alternating-permutation checks.

All geometric coefficients are exact rational values; the common square-root-two
factor of edge facet areas is factored out. Finite verification does not prove
claims for unbounded dimension; that proof is in RESULT.md.
"""
from fractions import Fraction as Q
from math import factorial, comb, pi, sqrt
from itertools import permutations


def compose_one_minus(coeffs):
    out = [Q(0)] * len(coeffs)
    for j, a in enumerate(coeffs):
        for k in range(j + 1):
            out[k] += a * comb(j, k) * (-1) ** k
    return out


def polynomial_product(a, b):
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def integrate_unit(a):
    return sum((coef / (i + 1) for i, coef in enumerate(a)), Q(0))


def polynomials(N):
    A = [[Q(1)]]
    for _ in range(N):
        reflected = compose_one_minus(A[-1])
        A.append([Q(0)] + [coef / (k + 1) for k, coef in enumerate(reflected)])
    return A


def data(n, A):
    a = [sum(v) for v in A]
    coordinate = [a[i - 1] * a[n - i] for i in range(1, n + 1)]
    # Edge area is sqrt(2) times the entries in edge_rational.
    edge_rational = [integrate_unit(polynomial_product(
        compose_one_minus(A[i - 1]), A[n - i - 1])) for i in range(1, n)]
    return a[n], coordinate, edge_rational


def alternating_permutations(n):
    for p in permutations(range(1, n + 1)):
        if all((p[i] < p[i + 1]) if (i % 2 == 0) else (p[i] > p[i + 1])
               for i in range(n - 1)):
            yield p


def main():
    A = polynomials(40)
    cases = facets_checked = 0
    for n in range(2, 10):
        volume, coord, edge = data(n, A)
        alt = list(alternating_permutations(n))
        assert volume == Q(len(alt), factorial(n)), (n, 'volume')
        for i, area in enumerate(coord, start=1):
            # Removing vertex i splits the path into two independent subpaths.
            ci = comb(n-1, i-1) * sum(1 for _ in alternating_permutations(i-1)) * sum(1 for _ in alternating_permutations(n-i))
            assert area == Q(ci, factorial(n-1)), (n,i,'coordinate')
            facets_checked += 1
        for i, rational_area in enumerate(edge, start=1):
            count = sum(abs(p[i-1]-p[i]) == 1 for p in alt)
            assert rational_area == Q(count, factorial(n-1)), (n,i,'edge')
            facets_checked += 1
        assert sum(coord) == 2 * n * volume, (n, 'coordinate total')
        assert sum(edge) == n * volume, (n, 'edge total')
        cases += 1
    n = 40
    volume, coord, edge = data(n, A)
    floatvol = float(volume)
    ctarget = [pi/2, pi*pi/4, 2]
    etarget = [pi/sqrt(2), sqrt(2)*(pi*pi/4-pi/2), sqrt(2)]
    cmeasure = [float(coord[j])/floatvol for j in (0,1,n//2)]
    emeasure = [sqrt(2)*float(edge[j])/floatvol for j in (0,1,n//2-1)]
    assert all(abs(x-y)<0.0001 for x,y in zip(cmeasure,ctarget)),cmeasure
    assert all(abs(x-y)<0.0001 for x,y in zip(emeasure,etarget)),emeasure
    print(f'PATH_FACET_AREA_PASS dimensions={cases} facets={facets_checked} independent_bond_counts=YES exact_total_identities=YES n40_asymptotic=YES')
    print('n40_coord_normalized:', [round(v,9) for v in cmeasure])
    print('n40_edge_normalized:', [round(v,9) for v in emeasure])

if __name__=='__main__':
    main()
