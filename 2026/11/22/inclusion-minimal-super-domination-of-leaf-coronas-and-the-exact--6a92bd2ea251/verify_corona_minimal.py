"""Independent exhaustive finite checks for inclusion-minimal super domination.

Standard library only. Run: python3 verify_corona_minimal.py
The graph-neighborhood condition is tested without using the structural rule.
"""
from collections import Counter
from itertools import product
from math import comb
from random import Random


def corona_neighborhoods(n, edges):
    adj = [0] * (2 * n)
    for u, v in edges:
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    for u in range(n):
        adj[u] |= 1 << (n + u)
        adj[n + u] |= 1 << u
    return adj


def directly_superdom_complement(adj, omitted):
    full = (1 << len(adj)) - 1
    selected = full ^ omitted
    o = omitted
    while o:
        bit = o & -o
        if not any((adj[v] & omitted) == bit for v in range(len(adj)) if selected >> v & 1):
            return False
        o ^= bit
    return True


def directly_minimal_superdom_complement(adj, omitted):
    full = (1 << len(adj)) - 1
    if not directly_superdom_complement(adj, omitted):
        return False
    add = full ^ omitted
    while add:
        bit = add & -add
        if directly_superdom_complement(adj, omitted | bit):
            return False
        add ^= bit
    return True


def predicted_minimal(n, edges, omitted):
    A = {i for i in range(n) if omitted >> i & 1}
    B = {i for i in range(n) if omitted >> (n + i) & 1}
    if A & B:
        return False
    H = [set() for _ in range(n)]
    for u, v in edges:
        H[u].add(v)
        H[v].add(u)
    if any(H[u] & A for u in B):
        return False
    return all((H[v] & A) and (H[v] & B) for v in set(range(n)) - A - B)


def audit_instance(n, edges):
    adj = corona_neighborhoods(n, edges)
    frequencies = Counter()
    for omitted in range(1 << (2 * n)):
        direct = directly_minimal_superdom_complement(adj, omitted)
        classified = predicted_minimal(n, edges, omitted)
        if direct != classified:
            raise AssertionError((n, edges, omitted, direct, classified))
        if direct:
            frequencies[2*n-omitted.bit_count()] += 1
    return frequencies


def formula(n):
    counts = Counter({n: 2})
    for j in range(1, n//4+1):
        numerator = n*comb(n-2*j-1,2*j-1)
        assert numerator % j == 0
        counts[n+2*j] = numerator//j
    return counts


def cycle_edges(n):
    return [(i, (i+1) % n) for i in range(n)]


def run():
    total = 0
    for n in range(1, 5):
        pairs = [(i, j) for i in range(n) for j in range(i+1, n)]
        for mask in range(1 << len(pairs)):
            edges = [p for i, p in enumerate(pairs) if mask >> i & 1]
            audit_instance(n, edges)
            total += 1
    print('ALL_LABELED_BASES_EXACT_SUBSET_CHECK_PASS', total)
    rng = Random(20261121)
    for n, samples in [(5,60), (6,16)]:
        pairs = [(i,j) for i in range(n) for j in range(i+1,n)]
        for _ in range(samples):
            edges = [p for p in pairs if rng.randrange(2)]
            audit_instance(n, edges)
        print('RANDOM_BASES_DIRECT_CHECK_PASS', n, samples)
    for n in range(3, 9):
        actual = audit_instance(n, cycle_edges(n))
        expected = formula(n)
        assert actual == expected, (n, actual, expected)
        print('CYCLE_DIRECT_ALL_SUBSETS_PASS', n, dict(sorted(actual.items())))
    for n in range(9, 14):
        edges = cycle_edges(n)
        adj = corona_neighborhoods(n, edges)
        actual = Counter()
        # Enumerate all at-most-one-omission-per-private-pair profiles.
        for word in product((0,1,2),repeat=n):
            O = sum(1<<i for i,s in enumerate(word) if s == 1)
            O |= sum(1<<(n+i) for i,s in enumerate(word) if s == 2)
            if directly_minimal_superdom_complement(adj,O):
                actual[2*n - O.bit_count()] += 1
        expected = formula(n)
        assert actual == expected,(n,actual,expected)
        print('CYCLE_ALL_PROFILE_CHECK_PASS',n, dict(sorted(actual.items())))
    for n in range(3,150):
        p = formula(n)
        assert min(p) == n
        assert max(p) == n+2*(n//4)
        assert all(p[s] > 0 for s in range(n, n+2*(n//4)+1,2))
        assert p[max(p)] == (2*n*comb(n-2*(n//4)-1, 2*(n//4)-1)//(2*(n//4)) if n>=4 else 2)
    print('INTEGER_FORMULA_AND_EXACT_SPECTRUM_PASS',147)
    print('VERIFY_OK')

if __name__ == '__main__':
    run()
