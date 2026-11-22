#!/usr/bin/env python3
"""Finite exhaustive checks for reversing roots of monotone idempotents."""
from collections import Counter, defaultdict
from itertools import combinations_with_replacement
from math import comb


def poly_H(L, R):
    return tuple((j+1)*comb(L, j)*comb(R, j)
                 for j in range(min(L, R)+1))


def multiply(a, b):
    c = [0]*(len(a)+len(b)-1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            c[i+j] += ai*bj
    return tuple(c)


def roots_polynomial(e):
    """Predicted distribution by excess image rank for f^2=e."""
    n = len(e)
    roots = sorted(set(e))
    sides = []
    for s in roots:
        fiber = [i for i in range(n) if e[i] == s]
        assert e[s] == s and fiber == list(range(fiber[0], fiber[-1]+1))
        sides.append((s-fiber[0], fiber[-1]-s))
    poly = (1,)
    k = len(roots)
    for i in range(k//2):
        L, R = sides[i]
        L2, R2 = sides[k-1-i]
        poly = multiply(poly, poly_H(L, R2))
        poly = multiply(poly, poly_H(R, L2))
    if k % 2:
        L, R = sides[k//2]
        poly = multiply(poly, poly_H(L, R))
    return poly


def ranked_theorem(n, k, r):
    if not 1 <= k <= r <= n:
        return 0
    return comb(k+r-1, r-k)*comb(n+k-1, 2*r-1) if 2*r-1 <= n+k-1 else 0


def compose(f, g):
    return tuple(f[g[i]] for i in range(len(f)))


def brute_two_rails(L, R):
    """Independently enumerate weakly increasing paired side maps."""
    out = Counter()
    for al in combinations_with_replacement(range(R+1), L):
        a = (0,)+al
        for br in combinations_with_replacement(range(L+1), R):
            b = (0,)+br
            if a[b[R]] == 0 and b[a[L]] == 0:
                j = len(set(a)) - 1 + len(set(b)) - 1
                out[j] += 1
    return tuple(out.get(j,0) for j in range(min(L, R)+1))


def main():
    for L in range(7):
        for R in range(7):
            assert brute_two_rails(L, R) == poly_H(L, R), (L,R)
    print('PAIRED_RAIL_KERNEL_EXHAUSTIVE_OK L,R <= 6')

    for n in range(1, 10):
        per_idempotent = defaultdict(Counter)
        antitone_ranks = Counter()
        isotone_ranks = Counter()
        for a in combinations_with_replacement(range(n), n):
            for kind, f in [('increasing',a), ('decreasing',a[::-1])]:
                e = compose(f, f)
                if compose(e,e) != e:
                    continue
                assert len(set(e)) <= len(set(f))
                k, r = len(set(e)), len(set(f))
                if kind == 'decreasing':
                    assert all(e[i] <= e[i+1] for i in range(n-1))
                    antitone_ranks[k,r] += 1
                    per_idempotent[e][r-k] += 1
                else:
                    assert compose(f,e) == e
                    isotone_ranks[k,r] += 1
        idem_count = 0
        for e in combinations_with_replacement(range(n), n):
            if compose(e,e) != e:
                continue
            idem_count += 1
            expected = roots_polynomial(e)
            actual = per_idempotent[e]
            assert all(actual.get(j,0)==expected[j] for j in range(len(expected))), (n,e,actual,expected)
            assert all(j < len(expected) for j in actual), (n,e,actual,expected)
        expected_ranks = Counter({(k,r):ranked_theorem(n,k,r)
                                  for k in range(1,n+1) for r in range(k,n+1)
                                  if ranked_theorem(n,k,r)})
        assert antitone_ranks == isotone_ranks == expected_ranks, (n,antitone_ranks,isotone_ranks,expected_ranks)
        print(f'n={n} idempotent_targets={idem_count} antitone_solutions={sum(antitone_ranks.values())} rank_cells={len(expected_ranks)} POINTWISE_AND_RANK_OK')
    print('ANTITONE_SQUARE_ROOT_THEOREM_FINITE_CHECKS_PASSED')

if __name__ == '__main__':
    main()
