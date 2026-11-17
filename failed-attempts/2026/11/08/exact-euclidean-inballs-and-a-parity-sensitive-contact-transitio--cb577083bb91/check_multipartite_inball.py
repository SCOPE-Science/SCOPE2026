"""Finite enumerative checks of centered Euclidean facet shells of multipartite root polytopes.

Requires only Python standard library. The analytical theorem does not depend on these checks.
"""
from fractions import Fraction
from itertools import product
from math import comb


def predicted(parts):
    n = sum(parts)
    l = max(parts)
    binary = Fraction((n // 2) * ((n + 1) // 2), n)
    ternary = Fraction(l) - Fraction(l % 2, n) if l >= 2 else Fraction(0)
    best = max(binary, ternary)
    count = 0
    if best == binary:
        count += comb(n, n // 2) * (2 if n % 2 else 1)
    if best == ternary and l >= 2:
        count += sum(x == l for x in parts) * comb(l, l // 2) * (2 if l % 2 else 1)
    return best, count


def exact_facet_norms(parts):
    n = sum(parts)
    klass = [i for i, s in enumerate(parts) for _ in range(s)]
    edges = [(i, j) for i in range(n) for j in range(i+1, n) if klass[i] != klass[j]]
    norms = []
    for f in product((0, 1, 2), repeat=n):
        if min(f) != 0 or max(f) == 0: continue
        if any(abs(f[i] - f[j]) > 1 for i, j in edges): continue
        adj = [[] for _ in range(n)]
        for i, j in edges:
            if abs(f[i] - f[j]) == 1:
                adj[i].append(j); adj[j].append(i)
        visited = {0}; stack = [0]
        while stack:
            for v in adj[stack.pop()]:
                if v not in visited:
                    visited.add(v); stack.append(v)
        if len(visited) != n: continue
        norms.append(Fraction(n*sum(t*t for t in f) - sum(f)**2, n))
    assert norms
    return max(norms), sum(v == max(norms) for v in norms), len(norms)


def integer_partitions(n, low=1):
    yield (n,)
    for k in range(low, n//2+1):
        for tail in integer_partitions(n-k, k):
            yield (k,) + tail


def main():
    tested = 0
    for n in range(3, 10):
        for parts in set(integer_partitions(n)):
            if len(parts) < 3: continue
            actual, count, facets = exact_facet_norms(parts)
            expected, predicted_count = predicted(parts)
            assert actual == expected, (parts,actual,expected)
            assert count == predicted_count, (parts,count,predicted_count)
            assert facets > 0
            tested += 1
    examples = {
        (2,2,2,2): (Fraction(2), 78),
        (2,2,2): (Fraction(2), 6),
        (3,3,3,3): (Fraction(3), 924),
        (1,1,1,1,1): (Fraction(6,5),20),
        (3,3,3): (Fraction(26,9),18),
    }
    for parts, pair in examples.items():
        assert predicted(parts) == pair, (parts,predicted(parts),pair)
    print('MULTIPARTITE_SYMMETRIC_EDGE_INBALL_CHECKS_PASSED', tested, 'cases')

if __name__ == '__main__':
    main()
