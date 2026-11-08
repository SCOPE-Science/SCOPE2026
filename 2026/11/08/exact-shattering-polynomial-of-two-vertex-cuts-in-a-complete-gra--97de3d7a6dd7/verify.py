#!/usr/bin/env python3
"""Independent finite checks for fixed-two-vertex cut traces (stdlib only)."""
from itertools import combinations
from collections import Counter
from math import comb


def signature(edges):
    if not edges:
        return ()
    neighbors = {}
    for u, v in edges:
        neighbors.setdefault(u, set()).add(v)
        neighbors.setdefault(v, set()).add(u)
    remaining = set(neighbors)
    comps = []
    while remaining:
        source = min(remaining)
        seen = {source}
        frontier = [source]
        while frontier:
            for w in neighbors[frontier.pop()]:
                if w not in seen:
                    seen.add(w)
                    frontier.append(w)
        remaining.difference_update(seen)
        degrees = tuple(sorted(len(neighbors[v]) for v in seen))
        comps.append((len(seen), sum(degrees) // 2, degrees))
    return tuple(sorted(comps))


P3 = (3, 2, (1, 1, 2))
K2 = (2, 1, (1, 1))
SHAPES3 = {
    ((4, 3, (1, 1, 1, 3)),),
    ((4, 3, (1, 1, 2, 2)),),
    tuple(sorted((P3, K2))),
}
SHAPES4 = {
    ((5, 4, (1, 1, 1, 1, 4)),),
    ((5, 4, (1, 1, 1, 2, 3)),),
    ((5, 4, (1, 1, 2, 2, 2)),),
    (P3, P3),
}


def predicted(n, es):
    s = len(es)
    if s == 0:
        return True
    if s == 1:
        return n >= 3
    if s == 2:
        return n >= 5
    if s == 3:
        return n >= 6 and signature(es) in SHAPES3
    if s == 4:
        sig = signature(es)
        active = len({v for e in es for v in e})
        return sig in SHAPES4 and n >= (active + (1 if sig == tuple(sorted((P3, K2))) else 2))
    return False


def actual(n, es):
    need = 1 << len(es)
    traces = set()
    for u, v in combinations(range(n), 2):
        mask = sum(1 << i for i, (a, b) in enumerate(es)
                   if (a == u or a == v) != (b == u or b == v))
        traces.add(mask)
        if len(traces) == need:
            return True
    return False


def polynomial(n):
    m = comb(n, 2)
    return [1, m, comb(m, 2) if n >= 5 else 0,
            (16 * comb(n, 4) + 30 * comb(n, 5)) if n >= 6 else 0,
            (125 * comb(n, 5) if n >= 7 else 0) +
            (90 * comb(n, 6) if n >= 8 else 0)]


def main():
    cases = 0
    for n in range(3, 9):
        universe = list(combinations(range(n), 2))
        counts = [0] * 5
        for s in range(5):
            for es in combinations(universe, s):
                p = predicted(n, es)
                a = actual(n, es)
                assert p == a, (n, es, p, a)
                cases += 1
                counts[s] += int(a)
        assert counts == polynomial(n), (n, counts, polynomial(n))
        print('n=', n, 'coefficients=', counts)
    # Directly validate 5-query impossibility for small n; all n proved by bound.
    for n in range(3, 7):
        edges = list(combinations(range(n), 2))
        for es in combinations(edges, 5):
            assert not actual(n, es)
            cases += 1
    print('TWO_VERTEX_CUTS_PASS', cases, 'supports including every size <=4 through n=8')


if __name__ == '__main__':
    main()
