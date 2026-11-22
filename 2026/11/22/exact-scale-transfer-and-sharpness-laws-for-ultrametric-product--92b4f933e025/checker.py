"""Exact finite tests for covering products of hierarchical metric spaces.

The script uses integer-power distance comparisons and an exact bitmask
set-cover solver. It is supplementary to the analytic proof.
"""
from functools import lru_cache
from itertools import product
from random import Random


def ultrametric(n, rng, upper=6):
    distances = [[0] * n for _ in range(n)]

    def fill(indices, height):
        if len(indices) <= 1:
            return
        if height == 1:
            for i in indices:
                for j in indices:
                    if i != j:
                        distances[i][j] = 1
            return
        shuffled = list(indices)
        rng.shuffle(shuffled)
        count = rng.randrange(1, min(3, len(indices)) + 1)
        groups = [shuffled[j::count] for j in range(count)]
        for a in range(count):
            for b in range(a + 1, count):
                for i in groups[a]:
                    for j in groups[b]:
                        distances[i][j] = distances[j][i] = height
        for g in groups:
            fill(g, height - 1)

    fill(list(range(n)), upper)
    return distances


def two_level(sizes, within, apart=7):
    labels = [i for i, size in enumerate(sizes) for _ in range(size)]
    matrix = [[0] * len(labels) for _ in labels]
    for i in range(len(labels)):
        for j in range(len(labels)):
            if i != j:
                matrix[i][j] = within[labels[i]] if labels[i] == labels[j] else apart
    return matrix


def classes(matrix, radius):
    unseen = set(range(len(matrix)))
    result = []
    while unseen:
        representative = min(unseen)
        group = [i for i in range(len(matrix)) if matrix[i][representative] <= radius]
        assert set(group) <= unseen, 'Not an ultrametric partition'
        result.append(group)
        unseen.difference_update(group)
    return result


def cov_by_mask(distance, power, radius_power):
    n = len(distance)
    if n == 0:
        return 0
    masks = []
    for c in range(n):
        mask = sum((1 << j) for j in range(n) if distance[c][j] <= radius_power)
        masks.append(mask)
    masks = sorted(set(masks), key=lambda x: (-x.bit_count(), x))
    complete = (1 << n) - 1
    memberships = [[mask for mask in masks if mask & (1 << j)] for j in range(n)]

    @lru_cache(None)
    def recurse(uncovered):
        if not uncovered:
            return 0
        candidates = [(len(memberships[i]), i) for i in range(n) if uncovered & (1 << i)]
        _, i = min(candidates)
        return 1 + min(recurse(uncovered & ~mask) for mask in memberships[i])

    return recurse(complete)


def product_power_distances(x, y, p):
    result = []
    for a, b in product(range(len(x)), range(len(y))):
        result.append([x[a][c]**p + y[b][d]**p
                       for c, d in product(range(len(x)), range(len(y)))])
    return result


def predicted(x, y, r, p):
    result = 0
    for cx in classes(x, r):
        m = len(cx)
        a = x[cx[0]][cx[-1]] if m > 1 else 0
        assert all(x[i][j] == a for i in cx for j in cx if i != j)
        for cy in classes(y, r):
            t_power = r**p - a**p
            y_cover = cov_by_mask([[y[i][j]**p for j in cy] for i in cy], p, t_power)
            result += min(m, y_cover)
    return result


def equality_predicted(x, y, r, p):
    diameters = []
    for mat in (x, y):
        diameters.append(max(max(mat[a][b] for a in c for b in c)
                             for c in classes(mat, r)))
    return diameters[0]**p + diameters[1]**p <= r**p


def main():
    rng = Random(260311)
    tests = 0
    equality_tests = 0
    for p in (1, 2, 3):
        for r in (2, 3, 4):
            for _ in range(48):
                k = rng.randint(1, 3)
                sizes = [rng.randint(1, 3) for _ in range(k)]
                while sum(sizes) > 5:
                    sizes[-1] = max(1, sizes[-1] - 1)
                    if sum(sizes) > 5:
                        sizes = sizes[:-1]
                within = [rng.randint(1, r) for _ in sizes]
                x = two_level(sizes, within, apart=7)
                y = ultrametric(rng.randint(1, 5), rng, upper=6)
                if len(x) * len(y) > 20:
                    continue
                actual = cov_by_mask(product_power_distances(x, y, p), p, r**p)
                expected = predicted(x, y, r, p)
                assert actual == expected, (p, r, sizes, within, y, actual, expected)
                tests += 1
                eq = equality_predicted(x, y, r, p)
                target = len(classes(x, r)) * len(classes(y, r))
                assert (actual == target) == eq
                equality_tests += 1
            for _ in range(22):
                x = ultrametric(rng.randint(1, 4), rng, upper=6)
                y = ultrametric(rng.randint(1, 4), rng, upper=6)
                actual = cov_by_mask(product_power_distances(x, y, p), p, r**p)
                expected_equal = equality_predicted(x, y, r, p)
                product_covers = len(classes(x, r)) * len(classes(y, r))
                assert (actual == product_covers) == expected_equal
                assert actual >= product_covers
                equality_tests += 1
    print(f'PASS: {tests} exact hierarchical formulas and {equality_tests} exact equality checks')
    # A nontrivial multi-level example, with a factor of three beyond product cover counts.
    x = two_level([4], [3])
    y = two_level([3], [3])
    assert cov_by_mask(product_power_distances(x, y, 1), 1, 3) == 3
    print('PASS: equilateral 4 x 3 at radius 3 requires three product balls')
    u = two_level([3, 2], [3, 1], apart=7)
    v = two_level([2, 2], [1, 1], apart=3)
    for pow_ in (1, 2, 3):
        actual = cov_by_mask(product_power_distances(u, v, pow_), pow_, 3 ** pow_)
        assert actual == predicted(u, v, 3, pow_)
    assert cov_by_mask(product_power_distances(u, v, 1), 1, 3) == 5
    print('PASS: two-scale example has exactly five unit-sum-product covering balls')


if __name__ == '__main__':
    main()
