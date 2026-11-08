#!/usr/bin/env python3
"""Direct incidence checks and exact combinatorial recurrences.

Run with Python 3: python artifacts/verify.py
No third-party packages are required.
"""
from itertools import combinations
from math import comb, factorial


def unicyclic_connected(j):
    """Number of connected labelled unicyclic simple graphs on j vertices."""
    if j < 3:
        return 0
    total = 0
    for ell in range(3, j + 1):
        forest_count = 1 if ell == j else ell * j ** (j - ell - 1)
        total += comb(j, ell) * (factorial(ell - 1) // 2) * forest_count
    return total


def unicyclic_polynomials(m):
    """Return coefficients indexed by number of unicyclic components."""
    u = [[0] * (m // 3 + 1) for _ in range(m + 1)]
    u[0][0] = 1
    for size in range(1, m + 1):
        for j in range(3, size + 1):
            weight = comb(size - 1, j - 1) * unicyclic_connected(j)
            for c, number in enumerate(u[size - j]):
                if number:
                    u[size][c + 1] += weight * number
    return u


def formula_poly(n):
    assert n >= 2
    m = n - 1
    u = unicyclic_polynomials(m)
    out = [0] * (m // 3 + 1)
    for k in range(1, m + 1):
        weight = n * comb(m, k) * (k + 1) ** (k - 1)
        for c, count in enumerate(u[m - k]):
            out[c] += weight * count
    return tuple(out)


def classify_pseudoforest(n, omitted, edges, F):
    adj = [[] for _ in range(n)]
    for e in F:
        a, b = edges[e]
        adj[a].append(b)
        adj[b].append(a)
    if not adj[omitted]:
        return None
    seen = set()
    cycles = 0
    for start in range(n):
        if start in seen:
            continue
        component = [start]
        seen.add(start)
        for v in component:
            for u in adj[v]:
                if u not in seen:
                    seen.add(u)
                    component.append(u)
        vcount = len(component)
        ecount = sum(len(adj[v]) for v in component) // 2
        if omitted in component:
            if ecount != vcount - 1:
                return None
        else:
            if ecount != vcount:
                return None
            cycles += 1
    return cycles


def exact_matching_count(n, omitted, edges, F):
    """Directly enumerate perfect matchings of the induced incidence graph."""
    U = frozenset(range(n)) - {omitted}
    F = tuple(F)
    # Domination of omitted original and all omitted subdividing vertices.
    if not any(omitted in edges[e] for e in F):
        return 0
    fset = set(F)
    if any((a not in U and b not in U) for i, (a, b) in enumerate(edges) if i not in fset):
        return 0

    def match(pos, available):
        if pos == len(F):
            return int(not available)
        a, b = edges[F[pos]]
        count = 0
        if a in available:
            count += match(pos + 1, available - {a})
        if b in available:
            count += match(pos + 1, available - {b})
        return count

    return match(0, U)


def run():
    # Exact all-subset search at the known minimum size; no guessed matchings.
    for n in range(2, 8):
        edges = list(combinations(range(n), 2))
        poly = [0] * len(formula_poly(n))
        cases = 0
        for omitted in range(n):
            for F in combinations(range(len(edges)), n - 1):
                cases += 1
                c = classify_pseudoforest(n, omitted, edges, F)
                count = exact_matching_count(n, omitted, edges, F)
                assert (0 if c is None else 2 ** c) == count, (n, omitted, F, c, count)
                if c is not None:
                    poly[c] += 1
        assert tuple(poly) == formula_poly(n), (n, poly, formula_poly(n))
        assert poly[0] == n ** (n - 1)
        print('DIRECT_INCIDENCE_OK', n, 'cases', cases, 'poly', tuple(poly))
    for n in range(2, 31):
        poly = formula_poly(n)
        assert poly[0] == n ** (n - 1)
        assert (sum(poly) > poly[0]) == (n >= 5)
        assert all(x >= 0 for x in poly)
    assert unicyclic_connected(3) == 1
    assert unicyclic_connected(4) == 15
    print('EXACT_RECURRENCE_AND_FIRST_MULTIPLE_MATCHING_THRESHOLD_OK n=2..30')
    print('VERIFY_OK')


if __name__ == '__main__':
    run()
