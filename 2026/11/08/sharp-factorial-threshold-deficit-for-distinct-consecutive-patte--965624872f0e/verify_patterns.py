"""Independent finite checks for distinct order-isomorphic consecutive windows.

Python 3, standard library only. Tests check finite statements; the
asymptotic theorem depends on the analytic proof in RESULT.md.
"""
from fractions import Fraction
from itertools import permutations
from math import factorial


def order_type(word):
    ranks = {v: j for j, v in enumerate(sorted(word))}
    return tuple(ranks[v] for v in word)


def distinct_count(p):
    n = len(p)
    return [len({order_type(p[i:i+k]) for i in range(n-k+1)})
            for k in range(1, n+1)]


def max_disjoint_aligned_indices(k, d):
    # A maximum matching in the forest of shift-d edges, checked by finite search.
    edges = [(j, j+d) for j in range(k)]
    best = ()
    for mask in range(1 << k):
        chosen = tuple(j for j in range(k) if mask >> j & 1)
        used = set()
        okay = True
        for j in chosen:
            if j in used or j+d in used:
                okay = False
                break
            used.add(j)
            used.add(j+d)
        if okay and len(chosen) > len(best):
            best = chosen
    return best


def checks():
    assertions = 0
    for n in range(2, 9):
        nfact = factorial(n)
        totals = [0] * n
        for p in permutations(range(n)):
            seq = distinct_count(p)
            for k, a in enumerate(seq, 1):
                assert a <= min(factorial(k), n-k+1)
                assertions += 1
                totals[k-1] += a
        if n == 3:
            assert sum(totals) == 22  # 11/3 expected distinct
            assertions += 1
        if n == 8:
            assert Fraction(sum(totals), nfact) < Fraction(n*(n+1), 2)
            assertions += 1
        print('n', n, 'expected_patterns', Fraction(sum(totals), nfact),
              'expected_deficit', Fraction(n*(n+1), 2) - Fraction(sum(totals), nfact))
    for k in range(2, 8):
        for d in range(1, k):
            chosen = max_disjoint_aligned_indices(k, d)
            assert len(chosen) >= k//2
            assert len(set(chosen) | {i+d for i in chosen}) == 2*len(chosen)
            assertions += 2
            if k+d > 8:
                continue
            collision = 0
            for p in permutations(range(k+d)):
                if order_type(p[:k]) == order_type(p[d:d+k]):
                    collision += 1
            assert Fraction(collision, factorial(k+d)) <= Fraction(1, factorial(len(chosen)))
            assertions += 1
            print('k,d', k, d, 'collision_probability', Fraction(collision, factorial(k+d)), 'disjoint_aligned', len(chosen))
    print('checked_assertions', assertions)


if __name__ == '__main__':
    checks()
