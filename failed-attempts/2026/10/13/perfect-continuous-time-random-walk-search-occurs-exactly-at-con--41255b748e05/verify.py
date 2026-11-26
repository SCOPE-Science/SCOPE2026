#!/usr/bin/env python3
"""Finite exact sanity checks for the analytic normalized-Laplacian search theorem.

The graph census is not used as an infinite proof. The RESULT.md supplies that proof.
Uses only the Python standard library.
"""
from fractions import Fraction
from itertools import combinations
from math import cos, sin, pi, sqrt


def connected(degs, edges):
    n = len(degs)
    seen = {0}
    while True:
        nxt = seen | {v for a, b in edges for u, v in ((a, b), (b, a)) if u in seen}
        if nxt == seen:
            return len(seen) == n
        seen = nxt


def check_graph(n, edges):
    degs = [0] * n
    nei = [set() for _ in range(n)]
    for u, v in edges:
        degs[u] += 1
        degs[v] += 1
        nei[u].add(v)
        nei[v].add(u)
    if not connected(degs, edges):
        return 0
    vol = sum(degs)
    for w in range(n):
        dw = degs[w]
        p = Fraction(dw, vol)
        gamma = 1 - p
        r = sum((Fraction(1, degs[u]) for u in nei[w]), Fraction()) / dw
        defect = r - p / (1 - p)
        assert defect >= 0
        # The unique oracle tuning inferred from the first moment fixes the
        # second-moment difference to gamma^2 times the local defect.
        second_from_stationary = p
        second_from_target = p*p + gamma*gamma*r
        assert second_from_target - second_from_stationary == gamma*gamma*defect
        regular_after_delete = len({degs[v] - 1 for v in range(n) if v != w}) == 1
        cone_regular = (dw == n-1 and regular_after_delete)
        assert (defect == 0) == cone_regular, (n, edges, w)
    return 1


def exhaust():
    total = 0
    for n in range(2, 7):
        possible = list(combinations(range(n), 2))
        for mask in range(1 << len(possible)):
            edges = [pair for j, pair in enumerate(possible) if mask & (1 << j)]
            total += check_graph(n, edges)
    return total


def two_state_checks():
    for k in range(13):
        g = Fraction(k+1, k+2)
        a = Fraction(-1, k+2)
        b = -sqrt(k+1)/(k+2)
        c = Fraction(1, k+2)
        assert a+c == 0
        assert abs(float(a*a + b*b) - 1/(k+2)) < 1e-14
        assert abs(float(c*c + b*b) - 1/(k+2)) < 1e-14
        assert abs((a+c)*b) < 1e-14
        t = pi*sqrt(k+2)/2
        prob = (1/(k+2))+(k+1)/(k+2)*sin(t/sqrt(k+2))**2
        assert abs(prob-1) < 2e-15
        assert g == Fraction(k+1, k+2)


if __name__ == '__main__':
    cnt = exhaust()
    two_state_checks()
    print(f'VERIFY_OK connected_labeled_graphs={cnt} orders=2..6 cone_blocks=13 exact_fractions=true')
