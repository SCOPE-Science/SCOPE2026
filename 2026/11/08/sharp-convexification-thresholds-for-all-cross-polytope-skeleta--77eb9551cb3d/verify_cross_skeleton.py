"""Exact arithmetic supplementary tests of the cross-polytope skeleton theorem.

No external dependencies. The universal statement is proved in RESULT.md.
"""
from fractions import Fraction as F
from itertools import combinations, product
from random import Random


def norm1(x):
    return sum((abs(v) for v in x), F(0))


def direct_support_distance(x, s):
    """Minimize over every support using an independent exact face formula."""
    n = len(x)
    b = None
    for size in range(1, s + 1):
        for I in combinations(range(n), size):
            t = sum((abs(x[i]) for i in I), F(0))
            # For fixed support/signs, best mass-one y has error |t-1| inside.
            a = norm1(x) - t + abs(t - 1)
            if b is None or a < b:
                b = a
    return b


def sorted_formula(x, s):
    q = norm1(x)
    top = sum(sorted((abs(v) for v in x), reverse=True)[:s], F(0))
    return q + 1 - 2 * min(F(1), top)


def threshold(d, s):
    return max(F(1), F(d, s) - 1)


def execute():
    rng = Random(20261102)
    counts = {'support_distances': 0, 'sharp_obstructions': 0,
              'coverage_samples': 0, 'boundary_cases': 0}
    for d in range(2, 8):
        for s in range(1, d + 1):
            L = threshold(d, s)
            for _ in range(75):
                v = tuple(F(rng.randrange(-10, 11), rng.randrange(1, 12)) for _ in range(d))
                assert direct_support_distance(v, s) == sorted_formula(v, s)
                counts['support_distances'] += 1
            assert sorted_formula((F(0),) * d, s) == 1
            assert L >= 1
            counts['boundary_cases'] += 1
            if L > 1:
                lam = (L + F(1)) / 2
                x = tuple((1 + lam) / d for _ in range(d))
                assert norm1(x) == 1 + lam
                assert sorted_formula(x, s) > lam
                counts['sharp_obstructions'] += 1
            else:
                lam = F(9, 10)
                assert sorted_formula((F(0),) * d, s) > lam
                counts['sharp_obstructions'] += 1
            for _ in range(70):
                weights = [rng.randrange(0, 25) for __ in range(d)]
                if sum(weights) == 0:
                    weights[0] = 1
                v = tuple(F(weights[j], sum(weights)) * (1 + L) * (1 if rng.randrange(2) else -1)
                          for j in range(d))
                q = norm1(v)
                assert q == 1 + L
                assert sorted_formula(v, s) <= L
                for z in (F(0), F(1, 4), F(1, 2), F(3, 4), F(1)):
                    assert sorted_formula(tuple(z * a for a in v), s) <= L
                    counts['coverage_samples'] += 1
    print('CROSS_SKELETON_EXACT_OK', counts, 'total', sum(counts.values()))


if __name__ == '__main__':
    execute()
