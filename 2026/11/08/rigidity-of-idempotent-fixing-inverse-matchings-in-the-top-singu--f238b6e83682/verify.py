"""Exact finite checks for inverse-match rigidity in isotone coatom classes.

Only Python's standard library is needed. This script independently computes
transformation composition and all mutual-inverse pairs, not just the claimed
index conditions. Exhaustive perfect-matching counts are finite corroboration;
the all-n theorem is proved separately by a coordinate-sum argument.
"""
from functools import lru_cache
from math import comb


def maps(n):
    out = {}
    for j in range(1, n):
        for k in range(1, n + 1):
            image = [z for z in range(1, n + 1) if z != k]
            out[j, k] = tuple(image[i - 1 if i <= j else i - 2]
                              for i in range(1, n + 1))
    return out


def compose(f, g):
    return tuple(f[x - 1] for x in g)


def mutually_inverse(f, g):
    return compose(compose(f, g), f) == f and compose(compose(g, f), g) == g


def mate(j, k):
    if k in (j, j + 1):
        return j, k
    if k > j + 1:
        return k - 1, j
    return k, j + 1


def perfect_matchings_count(n, actual_pairs):
    right = [(j, k) for j in range(1, n) for k in range(j + 2, n + 1)]
    left = [(j, k) for j in range(1, n) for k in range(1, j)]
    assert len(right) == len(left) == comb(n - 1, 2)
    idx = {x: i for i, x in enumerate(left)}
    adj = [sum(1 << idx[y] for y in left if (x, y) in actual_pairs) for x in right]

    @lru_cache(None)
    def count(i, occupied):
        if i == len(right):
            return 1
        pool = adj[i] & ~occupied
        total = 0
        while pool:
            bit = pool & -pool
            pool -= bit
            total += count(i + 1, occupied | bit)
        return total

    return count(0, 0), count.cache_info().currsize


def verify(n):
    F = maps(n)
    keys = list(F)
    pairs = {(x, y) for x in keys for y in keys
             if mutually_inverse(F[x], F[y])}
    idem = {x for x in keys if compose(F[x], F[x]) == F[x]}
    assert len(keys) == n * (n - 1)
    assert idem == {(j, k) for j in range(1, n) for k in (j, j + 1)}
    # No assumption that the proven index criterion is valid: verify it here.
    for j, k in keys:
        for u, v in keys:
            assert (((j, k), (u, v)) in pairs) == (
                v in (j, j + 1) and k in (u, u + 1))
    # Test the formula, involution property, idempotent preservation,
    # and reversal symmetry against actual transformation compositions.
    for x in keys:
        y = mate(*x)
        assert y in F and (x, y) in pairs and mate(*y) == x
        assert (y == x) == (x in idem)
        j, k = x
        reflected = (n - j, n + 1 - k)
        yy = mate(*reflected)
        u, v = y
        assert yy == (n - u, n + 1 - v)
    assert len(idem) == 2 * (n - 1)
    assert (len(keys) - len(idem)) // 2 == comb(n - 1, 2)
    out = f'n={n} elements={len(keys)} idempotents={len(idem)} pairs={len(pairs)} transpositions={comb(n - 1, 2)}'
    if n <= 8:
        number, states = perfect_matchings_count(n, pairs)
        assert number == 1
        out += f' fixed-idempotent-involutions={number} DP_states={states}'
    return out


if __name__ == '__main__':
    for n in range(4, 11):
        print(verify(n))
    print('VERIFY_OK direct_inverse_classes=7 exact_involution_counts=5')
