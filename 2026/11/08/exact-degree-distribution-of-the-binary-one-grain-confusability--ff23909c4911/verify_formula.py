"""Independent binomial run-composition and derivative census (n <= 18)."""
from collections import Counter
from math import comb


def choose(a, b):
    return comb(a, b) if 0 <= b <= a else 0


def run_composition_histogram(n):
    if n == 1:
        return {0: 2}
    N = n - 1
    counts = Counter()
    counts[N] += 2
    counts[2 * N - 1] += 2
    for k in range(1, N):
        zeros = N - k
        base = N + k * (zeros + 1)
        for r in range(N + 1):
            odd = choose(k - 1, r) * choose(zeros - 1, r)
            if odd:
                counts[base - (2 * r + 1)] += 2 * odd
                counts[base - (2 * r + 2)] += 2 * odd
            if r:
                even0 = choose(k - 1, r - 1) * choose(zeros - 1, r)
                even1 = choose(k - 1, r) * choose(zeros - 1, r - 1)
                if even0:
                    counts[base - 2 * r] += 2 * even0
                if even1:
                    counts[base - (2 * r + 1)] += 2 * even1
    return dict(counts)


def directly_enumerated_derivatives(n):
    if n == 1:
        return {0: 2}
    N = n - 1
    counts = Counter()
    for d in range(1 << N):
        t = [(d >> j) & 1 for j in range(N)]
        k = sum(t)
        b = sum(t[j] != t[j + 1] for j in range(N - 1))
        degree = N + k * (N - k + 1) - t[0] - b
        counts[degree] += 2
    return dict(counts)


if __name__ == '__main__':
    for n in range(1, 19):
        expected = run_composition_histogram(n)
        observed = directly_enumerated_derivatives(n)
        assert expected == observed, (n, expected, observed)
        assert sum(expected.values()) == 1 << n
        edges = sum(degree * count for degree, count in expected.items()) // 2
        expected_edges = ((n - 1) * (n + 2) * (1 << (n - 3))
                          if n >= 3 else (2 if n == 2 else 0))
        assert edges == expected_edges
        expected_max = n - 2 + n * n // 4 if n >= 3 else n - 1
        assert max(expected) == expected_max
        print(f'length={n} distinct_degrees={len(expected)} '
              f'max_degree={expected_max} edges={edges}')
    print('PASS: run-composition polynomial coefficients, full count, and edge identities.')
