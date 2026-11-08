"""Exact finite checks for two-output pairwise-proportional ranking compression.

Run: python verify.py.  Uses only Python's standard library.
"""
from itertools import combinations, permutations, product
from fractions import Fraction
from math import comb


def unanimity_edges(profile):
    n = len(profile)
    m = len(profile[0])
    positions = [{x: rank for rank, x in enumerate(p)} for p in profile]
    edges = {}
    for a, b in combinations(range(m), 2):
        count = sum(pos[a] < pos[b] for pos in positions)
        if count == n:
            edges[a, b] = (a, b)
        elif count == 0:
            edges[a, b] = (b, a)
    return edges


def matching_block_outputs(profile):
    m = len(profile[0])
    edges = list(unanimity_edges(profile).values())
    endpoints = [x for edge in edges for x in edge]
    if len(endpoints) != len(set(endpoints)):
        return None
    used = set(endpoints)
    blocks = sorted([[a, b] for a, b in edges] + [[a] for a in range(m) if a not in used], key=lambda b: min(b))
    return (tuple(x for block in blocks for x in block),
            tuple(x for block in reversed(blocks) for x in block))


def pairwise_prop(profile, outputs):
    n = len(profile)
    m = len(profile[0])
    ip = [{x: i for i, x in enumerate(p)} for p in profile]
    op = [{x: i for i, x in enumerate(p)} for p in outputs]
    for a, b in combinations(range(m), 2):
        s = sum(p[a] < p[b] for p in ip)
        t = sum(p[a] < p[b] for p in op)
        if s >= n and t < 2:
            return False
        if s >= n / 2 and t < 1:
            return False
        if n - s >= n and 2 - t < 2:
            return False
        if n - s >= n / 2 and 2 - t < 1:
            return False
    return True


def checks():
    checks = 0
    for m, n in [(3, 2), (3, 3), (4, 2), (4, 3)]:
        ranks = list(permutations(range(m)))
        for profile in product(ranks, repeat=n):
            edges = unanimity_edges(profile)
            out = matching_block_outputs(profile)
            matching = len(set(x for e in edges.values() for x in e)) == 2 * len(edges)
            assert (out is not None) == matching
            if out is not None:
                assert pairwise_prop(profile, out)
            # Mirror certificate exists exactly when no unanimous comparison.
            mirror = (ranks[0], tuple(reversed(ranks[0])))
            assert pairwise_prop(profile, mirror) == (len(edges) == 0)
            checks += 1
        print(f'EXHAUSTIVE m={m} n={n}: {len(ranks)**n} profiles')
    # Exact joint-consensus identity for two incident comparisons.
    for n in range(2, 6):
        ranks = list(permutations(range(3)))
        total = 0
        triple = 0
        for profile in product(ranks, repeat=n):
            e = unanimity_edges(profile)
            if (0, 1) in e and (0, 2) in e:
                total += 1
            if len(e) >= 2:
                triple += 1
        assert Fraction(total, 6 ** n) == 2*Fraction(1, 3**n) + 2*Fraction(1, 6**n)
        assert Fraction(triple, 6 ** n) == 6*Fraction(1, 3**n) - 6*Fraction(1, 6**n)
        print(f'EXACT m=3 n={n}: incident={total}, triple={triple} over {6**n}')
    print(f'PASS {checks} ranking profiles and exact incident-event identities')


if __name__ == '__main__':
    checks()
