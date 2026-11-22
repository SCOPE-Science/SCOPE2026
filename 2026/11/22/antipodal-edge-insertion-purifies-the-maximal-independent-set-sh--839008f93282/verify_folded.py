"""Independent exact finite verification of shattering after antipodal edge insertion.

Model: vertices 0..15, adjacency by XOR with allowed direction masks.
An integer's set bits identify a vertex subset. All 2^16 subsets are processed.
"""
from collections import Counter
from itertools import combinations, permutations

N = 16
FULL = (1 << N) - 1
D = (1, 2, 4, 8, 15)


def adjacency(directions):
    return [sum(1 << (x ^ d) for d in directions) for x in range(N)]


def independent(mask, adj):
    return all(not ((mask >> x) & 1) or not (mask & adj[x]) for x in range(N))


def is_maximal(mask, adj):
    return independent(mask, adj) and all((mask >> x) & 1 or (mask & adj[x]) for x in range(N))


def compute(directions):
    adj = adjacency(directions)
    concepts = [s for s in range(1 << N) if is_maximal(s, adj)]
    # All 65,536 subsets, not a sampled support collection.
    shattered = [False] * (1 << N)
    for s in range(1 << N):
        if (1 << s.bit_count()) <= len(concepts):
            shattered[s] = len({c & s for c in concepts}) == 1 << s.bit_count()
    facets = [s for s in range(1 << N) if shattered[s] and
              all(not shattered[s | (1 << x)] for x in range(N) if not ((s >> x) & 1))]
    polynomial = dict(sorted(Counter(s.bit_count() for s in range(1 << N) if shattered[s]).items()))
    return adj, concepts, shattered, facets, polynomial


def all_symmetries():
    sym = set()
    for p in permutations(D):
        lin = [0] * N
        for x in range(N):
            for i in range(4):
                if (x >> i) & 1:
                    lin[x] ^= p[i]
        if len(set(lin)) == N:
            for t in range(N):
                sym.add(tuple(lin[x] ^ t for x in range(N)))
    assert len(sym) == 1920
    return sym


def orbit(mask, sym):
    return {sum(1 << g[x] for x in range(N) if (mask >> x) & 1) for g in sym}


def trace_witnesses(support, concepts):
    S = sum(1 << x for x in support)
    answer = []
    for bits in range(1 << len(support)):
        trace = sum(1 << x for i, x in enumerate(support) if (bits >> i) & 1)
        witnesses = [c for c in concepts if c & S == trace]
        assert witnesses
        answer.append(min(witnesses))
    return answer


def main():
    a, concepts, shattered, facets, poly = compute(D)
    assert poly == {0: 1, 1: 16, 2: 80, 3: 160, 4: 120}
    assert Counter(s.bit_count() for s in concepts) == {4: 40, 5: 16}
    assert Counter(s.bit_count() for s in facets) == {4: 120}
    assert all(shattered[s] == (s.bit_count() <= 4 and independent(s, a)) for s in range(1 << N))
    sym = all_symmetries()
    R0, R1 = sum(1 << x for x in (0, 3, 5, 6)), sum(1 << x for x in (1, 2, 4, 8))
    o0, o1 = orbit(R0, sym), orbit(R1, sym)
    assert len(o0) == 40 and len(o1) == 80 and o0.isdisjoint(o1)
    assert o0 | o1 == set(facets)
    assert all(shattered[s] for s in o0 | o1)
    print('WITNESS_A', [f'{w:04x}' for w in trace_witnesses([0, 3, 5, 6], concepts)])
    print('WITNESS_B', [f'{w:04x}' for w in trace_witnesses([1, 2, 4, 8], concepts)])
    b, old, old_shattered, old_facets, old_poly = compute(D[:4])
    assert old_poly == {0: 1, 1: 16, 2: 88, 3: 160, 4: 104}
    assert Counter(s.bit_count() for s in old) == {4: 24, 5: 16, 8: 2}
    assert Counter(s.bit_count() for s in old_facets) == {2: 8, 4: 104}
    assert {s for s in old_facets if s.bit_count() == 2} == {(1 << x) | (1 << (x ^ 15)) for x in range(8)}
    print('FOLDED_FIVECUBE_MIS_SHATTER_PASS concepts=56 faces=1,16,80,160,120 facets=40+80')
    print('ANTIPODAL_PERTURBATION_PASS q4_facets=8x2+104x4 folded_facets=120x4')


if __name__ == '__main__':
    main()
