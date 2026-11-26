#!/usr/bin/env python3
"""Exhaustive independent rank-count checks for partial injections commuting with a square-zero map."""
from collections import Counter
from itertools import combinations, permutations
from math import comb, factorial


def partial_injections(n):
    for k in range(n + 1):
        for domain in combinations(range(n), k):
            for values in permutations(range(n), k):
                mapping = [-1] * n
                for source, target in zip(domain, values):
                    mapping[source] = target
                yield tuple(mapping)


def compose(left, right):
    return tuple(-1 if j == -1 else left[j] for j in right)


def cyclic(mapping):
    # Graph-theoretic detection, separate from the closed-form derivation.
    for start in range(len(mapping)):
        seen = set()
        current = start
        while current >= 0 and current not in seen:
            seen.add(current)
            current = mapping[current]
        if current >= 0:
            return True
    return False


def rook_polynomial(m):
    return [comb(m, j) ** 2 * factorial(j) for j in range(m + 1)]


def expected(r, s):
    n = 2 * r + s
    all_ranks = [0] * (n + 1)
    nil_ranks = [0] * (n + 1)
    for k in range(r + 1):
        m = r - k + s
        ways = comb(r, k) ** 2 * factorial(k)
        rook = rook_polynomial(m)
        nil_rook = rook[:]
        if s:
            for j, count in enumerate(rook_polynomial(m - 1)):
                nil_rook[j + 1] -= s * count
        nil_ways = (comb(r, k) * comb(r - 1, k) * factorial(k)
                    if k < r else (1 if r == 0 else 0))
        for j in range(m + 1):
            all_ranks[2 * k + j] += ways * rook[j]
            nil_ranks[2 * k + j] += nil_ways * nil_rook[j]
    return all_ranks, nil_ranks


def run():
    tests = []
    for n in range(1, 7):
        for r in range(n // 2 + 1):
            s = n - 2 * r
            f = tuple(i + r if i < r else -1 for i in range(n))
            c_counts, n_counts = Counter(), Counter()
            for g in partial_injections(n):
                if compose(f, g) == compose(g, f):
                    rank = sum(x >= 0 for x in g)
                    c_counts[rank] += 1
                    if not cyclic(g):
                        n_counts[rank] += 1
            observed = ([c_counts[j] for j in range(n + 1)],
                        [n_counts[j] for j in range(n + 1)])
            predicted = expected(r, s)
            assert observed == predicted, (n, r, s, observed, predicted)
            if r:
                assert predicted[0][n] == factorial(r) * factorial(s)
                assert predicted[1][n - 1] == factorial(r) * factorial(s)
            tests.append((r, s, sum(observed[0]), sum(observed[1])))
    for r, s, all_count, nil_count in tests:
        print(f"r={r} s={s} centralizer={all_count} nilpotent={nil_count} PASS")
    print(f"CASES={len(tests)}")
    print("ALL_ROOK_CENTRALIZER_NILPOTENT_RANK_CHECKS_PASS")


if __name__ == "__main__":
    run()
