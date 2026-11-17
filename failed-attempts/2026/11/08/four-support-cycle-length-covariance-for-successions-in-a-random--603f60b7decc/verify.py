"""Exact verification of the succession/cycle-length covariance identity.

All arithmetic is rational; no probabilistic simulation is used.
Run: python3 verify.py
"""
from fractions import Fraction
from itertools import permutations
from math import factorial


def predicted_local(n, i, j):
    assert n >= 4 and 1 <= i < n and 1 <= j <= n
    c = 1 if i in (1, n - 1) else 2
    total = Fraction(0)
    if j == 1:
        total += Fraction(c, n * (n - 1) * (n - 2))
    if j == 2:
        total += Fraction(1 - c, n * (n - 1) * (n - 3))
    if j == n - 1:
        total -= Fraction(n - 2 - c, n * (n - 1) * (n - 2) * (n - 3))
    if j == n:
        total += Fraction(1, n * n * (n - 1))
    return total


def predicted_total(n, j):
    assert n >= 4
    out = Fraction(0)
    if j == 1:
        out += Fraction(2, n * (n - 1))
    if j == 2 or j == n-1:
        out -= Fraction(1, n * (n - 1))
    if j == n:
        out += Fraction(1, n * n)
    return out


def conditional_moment(n, i, j):
    """Compute E[B_i C_j] from three compressed-path completions."""
    m = n - 2
    c = 1 if i in (1, n - 1) else 2
    # For a=i: two fixed points and a uniform permutation on m others.
    fixed = (Fraction(1, j) if j <= m else 0) + (2 if j == 1 else 0)
    # For a=i+/-1: one length-three path compressed to one marked vertex.
    chain = (Fraction(1, j) if j <= m else 0)
    if 1 <= j <= m:
        chain -= Fraction(1, m)
    if 3 <= j <= m + 2:
        chain += Fraction(1, m)
    # For other a: two length-two paths each compressed to a marked vertex.
    q = (Fraction(1, j) if j <= m else 0)
    if 2 <= j <= m + 1:
        q += Fraction(2, m)
    if 1 <= j <= m:
        q -= Fraction(2, m)
    def u(r):
        return r - 1 if 2 <= r <= m else 0
    q += Fraction(u(j - 2) - 2 * u(j - 1) + u(j), m * (m - 1))
    return Fraction(1, n * (n - 1)) * (fixed + c * chain + (m - c) * q)


def exact_brute(n):
    N = factorial(n)
    s_counts = [0] * (n - 1)
    c_counts = [0] * (n + 1)
    mixed = [[0] * (n + 1) for _ in range(n - 1)]
    for p in permutations(range(n)):
        cc = [0] * (n + 1)
        visited = [False] * n
        for v in range(n):
            if visited[v]:
                continue
            length = 0
            w = v
            while not visited[w]:
                visited[w] = True
                length += 1
                w = p[w]
            cc[length] += 1
        for j in range(1, n + 1):
            c_counts[j] += cc[j]
        for i in range(n - 1):
            if p[i + 1] == p[i] + 1:
                s_counts[i] += 1
                for j in range(1, n + 1):
                    mixed[i][j] += cc[j]
    return [
        [Fraction(mixed[i][j], N) - Fraction(s_counts[i] * c_counts[j], N * N)
         for j in range(1, n + 1)]
        for i in range(n - 1)
    ]


def run():
    checks = 0
    for n in range(4, 20):
        for i in range(1, n):
            for j in range(1, n + 1):
                # Analytic compression of forced paths, independently of the
                # simplified displayed covariance identity.
                calculated = conditional_moment(n, i, j) - Fraction(1, n * j)
                assert calculated == predicted_local(n, i, j), (n, i, j, calculated)
                checks += 1
        for j in range(1, n + 1):
            assert sum(predicted_local(n, i, j) for i in range(1, n)) == predicted_total(n, j)
            checks += 1
    for n in range(4, 10):
        empirical = exact_brute(n)
        for i in range(1, n):
            for j in range(1, n + 1):
                assert empirical[i - 1][j - 1] == predicted_local(n, i, j), (n, i, j)
                checks += 1
    print(f"PASS: {checks} exact rational comparisons; all permutations of sizes 4 through 9 enumerated")


if __name__ == '__main__':
    run()
