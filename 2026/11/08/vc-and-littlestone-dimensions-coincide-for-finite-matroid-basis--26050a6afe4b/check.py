"""Finite checks for basis-incidence shattering and deletion/contraction ranks.

This is corroboration for selected finite matroids, not a proof for all matroids.
Run with Python 3.9+: python check.py
"""
from itertools import combinations
from functools import lru_cache
from random import Random


def rank_of_vectors(columns):
    basis = {}
    for v in columns:
        w = v
        while w:
            k = w.bit_length() - 1
            if k in basis:
                w ^= basis[k]
            else:
                basis[k] = w
                break
    return len(basis)


def linear_bases(columns, r):
    return tuple(sum(1 << j for j in inds)
                 for inds in combinations(range(len(columns)), r)
                 if rank_of_vectors([columns[j] for j in inds]) == r)


def graphic_bases(vertices, edges):
    out = []
    for selected in combinations(range(len(edges)), vertices - 1):
        parent = list(range(vertices))
        def root(x):
            while x != parent[x]:
                x = parent[x]
            return x
        for i in selected:
            a, b = edges[i]
            a, b = root(a), root(b)
            if a != b:
                parent[a] = b
        if len({root(i) for i in range(vertices)}) == 1:
            out.append(sum(1 << j for j in selected))
    return tuple(out)


def ldim(concepts, n):
    patterns = tuple(sum(1 << i for i, b in enumerate(concepts) if b >> j & 1)
                     for j in range(n))
    @lru_cache(None)
    def rec(S):
        if not S or not S & (S - 1):
            return 0
        best = 0
        for mask in patterns:
            yes = S & mask
            no = S & ~mask
            if yes and no and min(yes.bit_count(), no.bit_count()) >= (1 << best):
                best = max(best, 1 + min(rec(yes), rec(no)))
        return best
    return rec((1 << len(concepts)) - 1)


def vc(concepts, n):
    for k in range(n, -1, -1):
        for J in combinations(range(n), k):
            traces = {sum(((B >> j) & 1) << i for i, j in enumerate(J))
                      for B in concepts}
            if len(traces) == (1 << k):
                return k
    raise AssertionError('nonempty class expected')


def dual_pair_distance(concepts):
    return max((a ^ b).bit_count() // 2 for a in concepts for b in concepts)


def rank_minimum(concepts, n):
    r = concepts[0].bit_count()
    vals = []
    for A in range(1 << n):
        rank = max((A & B).bit_count() for B in concepts)
        vals.append(2 * rank + n - A.bit_count() - r)
    return min(vals)


def test(name, concepts, n):
    concepts = tuple(sorted(set(concepts)))
    assert concepts and len({B.bit_count() for B in concepts}) == 1
    v = vc(concepts, n)
    ell = ldim(concepts, n)
    h = dual_pair_distance(concepts)
    mi = rank_minimum(concepts, n)
    assert v == ell == h == mi, (name, v, ell, h, mi)
    for e in range(n):
        yes = [B for B in concepts if (B >> e) & 1]
        no = [B for B in concepts if not (B >> e) & 1]
        if yes and no:
            assert 1 + min(dual_pair_distance(yes), dual_pair_distance(no)) == h
    print(f'{name}: bases={len(concepts)}, VC=Ldim=intersection-rank={v}, split identity OK')


def run():
    test('uniform U(2,5)', (sum(1 << j for j in J) for J in combinations(range(5), 2)), 5)
    test('uniform U(3,6)', (sum(1 << j for j in J) for J in combinations(range(6), 3)), 6)
    test('binary rank-3 Fano', linear_bases([1, 2, 3, 4, 5, 6, 7], 3), 7)
    test('graphic K4', graphic_bases(4, list(combinations(range(4), 2))), 6)
    test('graphic K(2,4)', graphic_bases(6, [(a, b) for a in range(2) for b in range(2, 6)]), 8)
    test('partition rank-2', (sum(1 << j for j in (a, b)) for a in (0, 1, 2) for b in (3, 4, 5)), 6)
    rng = Random(20261103)
    for i in range(20):
        cols = [rng.randrange(1, 16) for _ in range(8)]
        r = rank_of_vectors(cols)
        bases = linear_bases(cols, r)
        if bases:
            test(f'binary example {i+1}', bases, len(cols))
    nonmatroid = (22, 21, 28, 37, 19, 56, 50, 49, 11)
    assert vc(nonmatroid, 6) == 2 and ldim(nonmatroid, 6) == 3
    print('Nonmatroid constant-weight contrast: VC=2, Littlestone=3')
    print('ALL_MATROID_BASIS_CHECKS_PASS')


if __name__ == '__main__':
    run()
