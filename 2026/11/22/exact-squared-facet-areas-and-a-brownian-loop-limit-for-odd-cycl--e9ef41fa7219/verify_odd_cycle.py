"""Exact integer Gram verification of odd-cycle symmetric-edge facet areas.

Run: python verify_odd_cycle.py
Python 3 standard library only. Finite checks supplement, not replace, the proof.
"""
from fractions import Fraction
from itertools import combinations
from math import comb, factorial


def det_bareiss(matrix):
    a = [row[:] for row in matrix]
    n = len(a)
    if not n:
        return 1
    sign, prior = 1, 1
    for k in range(n - 1):
        if not a[k][k]:
            pivot = next((r for r in range(k + 1, n) if a[r][k]), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        p = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                top = a[i][j] * p - a[i][k] * a[k][j]
                assert top % prior == 0, (n, k, top, prior)
                a[i][j] = top // prior
        for i in range(k + 1, n):
            a[i][k] = 0
        prior = p
    return sign * a[n - 1][n - 1]


def facet_gram_det(n, signs):
    # Actual Euclidean signed-root simplex vertices, not the path-potential identity.
    roots = []
    for i, sign in enumerate(signs):
        v = [0] * n
        v[i], v[i + 1] = sign, -sign
        roots.append(v)
    base = roots[0]
    diffs = [[v[j] - base[j] for j in range(n)] for v in roots[1:]]
    gram = [[sum(x * y for x, y in zip(u, v)) for v in diffs] for u in diffs]
    return det_bareiss(gram)


def potential_area_num(n, signs):
    partial = [0]
    for s in signs:
        partial.append(partial[-1] + s)
    assert partial[-1] == 0
    return n * sum(x * x for x in partial) - sum(partial) ** 2


def verify():
    grand = 0
    for n in (3, 5, 7, 9):
        m = n - 1
        area_nums = []
        for positives in combinations(range(m), m // 2):
            positive = set(positives)
            signs = tuple(1 if j in positive else -1 for j in range(m))
            independent = facet_gram_det(n, signs)
            bridge = potential_area_num(n, signs)
            assert independent == bridge, (n, signs, independent, bridge)
            assert independent > 0
            area_nums.append(independent)
        assert len(area_nums) * n == n * comb(n - 1, (n - 1) // 2)
        mean_area_sq = Fraction(sum(area_nums), len(area_nums) * factorial(n - 2) ** 2)
        target = Fraction(n * (n * n - 1), 12 * factorial(n - 2) ** 2)
        assert mean_area_sq == target, (n, mean_area_sq, target)
        grand += n * len(area_nums)
        print(f'n={n}: facets={n * len(area_nums)} distinct_squared_area_classes={len(set(area_nums))} exact_mean={mean_area_sq}')
    print(f'ODD_CYCLE_FACET_AREA_EXACT_PASS facets={grand} n=3,5,7,9')


if __name__ == '__main__':
    verify()
