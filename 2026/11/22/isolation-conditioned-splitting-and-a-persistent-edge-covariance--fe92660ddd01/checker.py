"""Exact finite pairing checks for a uniform random interval graph.
No external dependencies. Runs in a few seconds at orders up to six.
"""
from collections import Counter
from fractions import Fraction
from math import comb, factorial


def pairings(positions):
    if not positions:
        yield ()
        return
    first = positions[0]
    for j in range(1, len(positions)):
        other = positions[j]
        remaining = positions[1:j] + positions[j + 1:]
        for tail in pairings(remaining):
            yield ((first, other),) + tail


def graph_data(pairs):
    m = len(pairs)
    deg = [0] * m
    edges = 0
    for i in range(m):
        a, b = pairs[i]
        for j in range(i + 1, m):
            c, d = pairs[j]
            if not (b < c or d < a):
                deg[i] += 1
                deg[j] += 1
                edges += 1
    return edges, deg


def rational_theorem(n):
    m = n - 1
    D = factorial(2 * n)
    w = [2 * comb(m, k) * factorial(2 * k) * factorial(2 * (m - k)) for k in range(n)]
    A = Fraction(sum(w), D)
    C = (Fraction(2, D) * sum(comb(n - 3, k) * factorial(2 * k + 2) * factorial(2 * (n - 3 - k) + 2)
                                  for k in range(n - 2))) if n >= 3 else Fraction(0)
    cov = -Fraction(2, 3) * n * m * (A + (m - 1) * C)
    return A, C, cov, [Fraction(x, D) for x in w]


def test():
    checks = 0
    hist = {0: Counter({0: 1})}
    for n in range(1, 7):
        zsum = esum = zesum = 0
        cond = Counter()
        pairs_count = 0
        hist[n] = Counter()
        for pairs in pairings(tuple(range(2 * n))):
            pairs_count += 1
            e, d = graph_data(pairs)
            hist[n][e] += 1
            z = sum(x == 0 for x in d)
            zsum += z
            esum += e
            zesum += z * e
            for a, (left, right) in enumerate(pairs):
                if d[a] == 0:
                    k = sum(r < left for j, (_, r) in enumerate(pairs) if j != a)
                    cond[(k, e)] += 1
        assert pairs_count == factorial(2 * n) // (2**n * factorial(n))
        checks += 1
        assert Fraction(esum, pairs_count) == Fraction(n * (n - 1), 3)
        checks += 1
        if n >= 2:
            A, C, cv, weight = rational_theorem(n)
            assert Fraction(zsum, n * pairs_count) == A
            checks += 1
            assert Fraction(zesum, pairs_count) - Fraction(zsum * esum, pairs_count**2) == cv
            checks += 1
            for k in range(n):
                assert Fraction(sum(v for (j, e), v in cond.items() if j == k), n * pairs_count) == weight[k]
                checks += 1
                left_hist = hist[k]
                right_hist = hist[n - 1 - k] if n - 1 - k in hist else None
                # The graph after deleting an isolated marked vertex consists
                # of independent interval graphs on k and n-1-k vertices.
                if right_hist is None:
                    right_hist = Counter()
                    for ps in pairings(tuple(range(2 * (n - 1 - k)))):
                        ee, _ = graph_data(ps)
                        right_hist[ee] += 1
                total_left = sum(left_hist.values())
                total_right = sum(right_hist.values())
                for e in range(comb(n - 1, 2) + 1):
                    expected = sum(left_hist[j] * right_hist[e - j] for j in left_hist if e - j in right_hist)
                    assert Fraction(cond[(k, e)], sum(v for (j, _), v in cond.items() if j == k)) == Fraction(expected, total_left * total_right)
                    checks += 1
        print('n', n, 'pairings', pairs_count, 'checks', checks)
    assert all(rational_theorem(n)[2] < 0 for n in range(2, 50))
    checks += 1
    print('PASS', checks, 'exact checks')


if __name__ == '__main__':
    test()
