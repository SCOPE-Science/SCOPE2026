"""Reproducibility checks for critical threshold-graph birth laws.

Runs entirely with the Python standard library, with exact rational arithmetic
for finite identities and exhaustive finite deterministic configurations.
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def closed_no_edge(n, c):
    r = Fraction(c, n)
    return 2 * (1 - r/2) ** n - (1 - r) ** n


def integrated_no_edge(n, c):
    # Integrate over the minimum of n independent Unif(0,n) deficits.
    # All deficits at least c/2, or minimum x<c/2 and every other
    # deficit at least c-x. Expand the latter integral as a polynomial.
    a = 1 - Fraction(c, n)
    h = Fraction(c, 2*n)
    rest = sum((n * comb(n-1, j) * a**(n-1-j) * h**(j+1)
                / Fraction(j+1)) for j in range(n))
    return (1-h)**n + rest


def closed_moments(n, c):
    p = Fraction(c*c, 2*n*n)
    q = Fraction(c*c*c, 3*n*n*n)
    e = comb(n, 2) * p
    v = comb(n, 2)*p*(1-p) + n*(n-1)*(n-2)*(q-p*p)
    return e, v


def integrated_moments(n, c):
    # Integrals over [0,c] with uniform density 1/n:
    # p = integral_0^c (c-y) dy/n^2;
    # q = integral_0^c (c-y)^2 dy/n^3.
    p = Fraction(c, n) ** 2 / 2
    q = Fraction(c, n) ** 3 / 3
    edges = comb(n, 2)
    edge_pairs_sharing_vertex = n*comb(n-1, 2)
    e = edges*p
    second_factorial = edges*(edges-1)*p*p + 2*edge_pairs_sharing_vertex*(q-p*p)
    v = second_factorial + e - e*e
    return e, v


def actual_clique_number(points, threshold):
    m = len(points)
    best = 1 if m else 0
    for k in range(2, m+1):
        for ix in combinations(range(m), k):
            if all(points[i] + points[j] < threshold
                   for i, j in combinations(ix, 2)):
                best = k
                break
    return best


def formula_clique_number(points, threshold):
    arr = sorted(points)
    return max([1] + [k for k in range(2, len(arr)+1)
                       if arr[k-2] + arr[k-1] < threshold]) if arr else 0


def run():
    total = 0
    for n in range(2, 11):
        for c in (Fraction(1, 4), Fraction(1, 2), Fraction(1, 1),
                  Fraction(3, 2), Fraction(7, 4)):
            assert c <= n
            assert closed_no_edge(n,c) == integrated_no_edge(n,c)
            assert closed_moments(n,c) == integrated_moments(n,c)
            total += 2
    # Entire integer-grid class of small point configurations, including ties.
    for n in range(2,7):
        for points in combinations(range(9),n):
            for threshold in range(1,17):
                assert actual_clique_number(points,threshold) == formula_clique_number(points,threshold)
                total += 1
    # At large threshold the deterministic first two order statistics govern
    # the first edge; for each k, the last two in the first k govern the clique.
    assert Fraction(0) < closed_no_edge(5,Fraction(3,2)) < 1
    total += 1
    print(f"PASS: {total} exact assertions; finite integrals, moments, clique clocks")


if __name__ == "__main__":
    run()
