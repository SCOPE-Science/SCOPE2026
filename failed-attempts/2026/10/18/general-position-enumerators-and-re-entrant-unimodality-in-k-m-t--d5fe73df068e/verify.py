"""Direct adjacency verification and exact arithmetic for product-graph general position.

Requires only Python 3 standard library. Run: python3 verify.py
"""
from collections import Counter
from math import comb, factorial


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def predicted(m, n):
    if not (m >= 3 and n >= 3):
        raise ValueError('both factor orders must be at least three')
    a, b = Counter(), Counter()
    for k in range(n + 1):
        a[k] += m * choose(n, k)
    for k in range(m + 1):
        a[k] += n * choose(m, k)
    a[0] -= m + n - 1
    a[1] -= m * n
    for k in range(2, min(m, n) + 1):
        a[k] += choose(m, k) * choose(n, k) * factorial(k)
    rectangles = choose(m, 2) * choose(n, 2)
    a[3] += 4 * rectangles
    a[4] += rectangles
    b[n] += m
    b[m] += n
    large, small = max(m, n), min(m, n)
    b[small] += factorial(large) // factorial(large - small)
    b[4] += rectangles
    return +a, +b


def enumerated(m, n):
    count = m * n
    neighbors = [0] * count
    for i in range(count):
        for j in range(count):
            if i // n != j // n and i % n != j % n:
                neighbors[i] |= 1 << j
    # A triple is forbidden iff the induced graph is a three-vertex path.
    bad_triples = []
    for a in range(count):
        for b in range(a + 1, count):
            for c in range(b + 1, count):
                e = (((neighbors[a] >> b) & 1) +
                     ((neighbors[a] >> c) & 1) +
                     ((neighbors[b] >> c) & 1))
                if e != 2:
                    continue
                deg = [((neighbors[x] >> y) & 1) + ((neighbors[x] >> z) & 1)
                       for x, y, z in ((a, b, c), (b, a, c), (c, a, b))]
                if sorted(deg) == [1, 1, 2]:
                    bad_triples.append((1 << a) | (1 << b) | (1 << c))
    a, b = Counter(), Counter()
    for subset in range(1 << count):
        if any((subset & forbidden) == forbidden for forbidden in bad_triples):
            continue
        a[subset.bit_count()] += 1
        # Saturation is tested by trying every unused vertex, not by a formula.
        if all(any(((subset | (1 << v)) & forbidden) == forbidden
                   for forbidden in bad_triples)
               for v in range(count) if (subset & (1 << v)) == 0):
            b[subset.bit_count()] += 1
    return +a, +b


def unimodal(values):
    sequence = [values.get(k, 0) for k in range(max(values) + 1)]
    return any(all(sequence[i] <= sequence[i + 1] for i in range(p))
               and all(sequence[i] >= sequence[i + 1]
                       for i in range(p, len(sequence) - 1))
               for p in range(len(sequence)))


def main():
    profiles = [(3, 3), (3, 4), (3, 5), (4, 4), (4, 5)]
    total_subsets = 0
    for m, n in profiles:
        calculated = enumerated(m, n)
        expected = predicted(m, n)
        assert calculated == expected, (m, n, calculated, expected)
        total_subsets += 1 << (m * n)
    # Exact-integer checks on structural consequences for 3 <= m <= n <= 25.
    facet_profiles = 0
    for m in range(3, 26):
        for n in range(m, 26):
            poly, facets = predicted(m, n)
            assert poly[0] == 1
            assert poly[1] == m * n
            assert poly[2] == choose(m * n, 2)
            assert set(facets) == {4, m, n}
            assert (len(facets) == 1) == (m == n == 4)
            facet_profiles += 1
    for n in range(3, 301):
        poly, _ = predicted(3, n)
        assert unimodal(poly) == (n <= 10 or n >= 18), n
        a3 = 9 * choose(n, 3) + 12 * choose(n, 2) + n
        a4 = 3 * choose(n, 4) + 3 * choose(n, 2)
        a5 = 3 * choose(n, 5)
        assert (poly[3], poly[4], poly[5]) == (a3, a4, a5)
        assert a3 > a4 if n <= 17 else a3 < a4
        assert a4 > a5 if n <= 10 else a4 < a5
    print('VERIFICATION_OK direct_profiles={} vertex_subsets={} facet_profiles={} three_by_n_orders=3..300'.format(
        len(profiles), total_subsets, facet_profiles))


if __name__ == '__main__':
    main()
