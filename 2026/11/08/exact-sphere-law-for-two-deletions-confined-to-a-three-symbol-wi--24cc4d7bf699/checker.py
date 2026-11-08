"""Independent finite checks for localized (2,3)-deletion sphere formulas.

Run: python checker.py
This verifier checks finite cases only; the all-length statements rely on the proof.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product


def direct_volume(x):
    n = len(x)
    outputs = set()
    for i in range(n):
        for j in range(i + 1, min(i + 3, n)):
            outputs.add(tuple(x[k] for k in range(n) if k != i and k != j))
    return len(outputs)


def formula_volume(x):
    n = len(x)
    distinct = sum(len({x[i], x[i + 1], x[i + 2]}) == 3 for i in range(n - 2))
    constant = sum(x[i] == x[i + 1] == x[i + 2] for i in range(n - 2))
    return n - 1 + distinct - constant


def theoretical_moments(q, n):
    mu = Fraction(q * q - 3 * q + 1, q * q)
    mean = n - 1 + (n - 2) * mu
    var = Fraction((q - 1) * (5 * n * q * q - 9 * n * q + 3 * n - 12 * q * q + 22 * q - 8), q ** 4)
    return mean, var


def finite_dist_by_matrix(q, n):
    # Independent transfer computation over ordered-pair states.
    d = {(a, b, 0): 1 for a in range(q) for b in range(q)}
    for _ in range(n - 2):
        nxt = defaultdict(int)
        for (a, b, k), v in d.items():
            for c in range(q):
                score = (len({a, b, c}) == 3) - (a == b == c)
                nxt[(b, c, k + score)] += v
        d = nxt
    ans = Counter()
    for (_, _, k), v in d.items():
        ans[n - 1 + k] += v
    return ans


def fib(k):
    a, b = 0, 1
    for _ in range(k):
        a, b = b, a + b
    return a


def run():
    instances = 0
    profiles = 0
    for q, max_n in ((2, 12), (3, 9), (4, 8), (5, 6)):
        for n in range(3, max_n + 1):
            dist = Counter()
            for x in product(range(q), repeat=n):
                a = direct_volume(x)
                b = formula_volume(x)
                assert a == b, (q, n, x, a, b)
                dist[a] += 1
                instances += 1
            assert sum(dist.values()) == q ** n
            mean = Fraction(sum(a * c for a, c in dist.items()), q ** n)
            var = Fraction(sum(a * a * c for a, c in dist.items()), q ** n) - mean ** 2
            assert (mean, var) == theoretical_moments(q, n), (q, n, mean, var)
            assert dist == finite_dist_by_matrix(q, n), (q, n, 'transfer mismatch')
            assert dist[1] == q, (q, n, 'minimum-count mismatch')
            if q == 2:
                assert max(dist) == n - 1
                assert dist[n - 1] == 2 * fib(n + 1)
            else:
                assert max(dist) == 2 * n - 3
                assert dist[2 * n - 3] == q * (q - 1) * (q - 2) ** (n - 2)
            profiles += 1
    print(f'PASS direct comparisons: {instances}; exact distribution/moment/extremum profiles: {profiles}')


if __name__ == '__main__':
    run()
