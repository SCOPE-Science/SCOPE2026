"""Finite checks for natural conjugacy in star partial-isometry monoids.

Python 3 standard library only. The finite enumeration tests the semigroup
conjugacy equations themselves; generating-function checks are independent.
"""
import itertools
from collections import Counter
from math import factorial


def partial_isometries(m):
    n = m + 1
    def distance(x, y):
        return 0 if x == y else 1 if 0 in (x, y) else 2
    out = []
    for k in range(n + 1):
        for domain in itertools.combinations(range(n), k):
            for values in itertools.permutations(range(n), k):
                if all(distance(domain[i], domain[j]) ==
                       distance(values[i], values[j])
                       for i in range(k) for j in range(i + 1, k)):
                    out.append(tuple(zip(domain, values)))
    return out


def compose(a, b):
    """Return a after b, for injective maps stored as ordered pairs."""
    lookup = dict(a)
    return tuple(sorted((x, lookup[y]) for x, y in b if y in lookup))


def inverse(a):
    return tuple(sorted((y, x) for x, y in a))


def direct_class_polynomial(m):
    maps = partial_isometries(m)
    positions = {a: i for i, a in enumerate(maps)}
    parent = list(range(len(maps)))
    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    def union(i, j):
        parent[find(i)] = find(j)
    for i, a in enumerate(maps):
        for g in maps:
            gi = inverse(g)
            b = compose(gi, compose(a, g))
            if compose(g, compose(b, gi)) == a:
                union(i, positions[b])
    groups = {}
    for i, a in enumerate(maps):
        groups.setdefault(find(i), []).append(a)
    counts = Counter(len(group[0]) for group in groups.values())
    class_sizes = sorted((len(group[0]), len(group)) for group in groups.values())
    return [counts.get(k, 0) for k in range(m + 2)], len(maps), class_sizes


def leaf_type_profile(m):
    """F_m(z): count cycle-chain profiles on at most m support vertices."""
    dp = [[0] * (m + 2) for _ in range(m + 1)]
    dp[0][0] = 1
    for size, rank in ([(j, j) for j in range(1, m + 1)] +
                       [(j, j - 1) for j in range(2, m + 1)]):
        for support in range(size, m + 1):
            for r in range(rank, m + 2):
                dp[support][r] += dp[support - size][r - rank]
    return [sum(dp[s][r] for s in range(m + 1)) for r in range(m + 2)]


def expected_class_polynomial(m):
    f = leaf_type_profile(m)
    return [f[r] + (f[r - 1] if r else 0) +
            ((1 if m == 1 else 2) if r == 2 else 0)
            for r in range(m + 2)]


def expected_class_sizes(m):
    types = [('c', j, j, j) for j in range(1, m + 1)] + \
            [('p', j, j - 1, 1) for j in range(2, m + 1)]
    out = []
    def rec(i, support, rank, denom, nonempty=False):
        if i == len(types):
            count = factorial(m) // (factorial(m - support) * denom)
            out.append((rank, count + int(support == 1 and rank == 1)))
            if nonempty:
                out.append((rank + 1, count))
            return
        typ, size, r, factor = types[i]
        for k in range((m - support) // size + 1):
            rec(i + 1, support + k * size, rank + k * r,
                denom * factor ** k * factorial(k),
                nonempty or k > 0)
    rec(0, 0, 0, 1)
    out.extend([(1, 2 * m), (2, m)])
    if m >= 2:
        out.append((2, m * (m - 1)))
    return sorted(out)


def two_color_partitions(m):
    dp = [0] * (m + 1)
    dp[0] = 1
    for size in range(1, m + 1):
        for _ in range(2):
            for s in range(size, m + 1):
                dp[s] += dp[s - size]
    return dp[m]


if __name__ == '__main__':
    for m in range(1, 5):
        observed, elements, class_sizes = direct_class_polynomial(m)
        predicted = expected_class_polynomial(m)
        assert observed == predicted, (m, observed, predicted)
        assert class_sizes == expected_class_sizes(m), (m, class_sizes, expected_class_sizes(m))
        print('leaves', m, 'elements', elements, 'rank-class-counts', observed)
    for m in range(2, 13):
        predicted = expected_class_polynomial(m)
        assert sum(predicted) == 2 * two_color_partitions(m) + 2
    for r in range(1, 6):
        left = expected_class_polynomial(2 * r - 1)[r]
        right = expected_class_polynomial(2 * r)[r]
        assert right - left == 1, (r, left, right)
        assert all(expected_class_polynomial(m)[r] == right
                   for m in range(2 * r, 13))
    print('STAR_NATURAL_CONJUGACY_CHECKS_PASSED')
