#!/usr/bin/env python3
"""Exact finite checks for spanning-tree overlap on complete bipartite graphs.

Uses only the Python standard library. Counts spanning trees independently by
enumerating edge subsets and testing acyclicity; does not use the transfer-current
formula to produce these counts.
"""

from collections import Counter
from fractions import Fraction
from itertools import combinations


assertions = 0


def check(condition, context):
    global assertions
    assertions += 1
    if not condition:
        raise AssertionError(context)


def is_tree(n, edges):
    parent = list(range(n))

    def root(v):
        while parent[v] != v:
            v = parent[v]
        return v

    for u, v in edges:
        ru, rv = root(u), root(v)
        if ru == rv:
            return False
        parent[ru] = rv
    return len({root(v) for v in range(n)}) == 1


def enumerate_and_check(a, b):
    edges = [(i, a + j) for i in range(a) for j in range(b)]
    degree = a + b - 1
    tree_count = 0
    single = [0] * len(edges)
    pair = Counter()
    for indices in combinations(range(len(edges)), degree):
        if not is_tree(a + b, [edges[k] for k in indices]):
            continue
        tree_count += 1
        for k in indices:
            single[k] += 1
        for k, l in combinations(indices, 2):
            pair[(k, l)] += 1

    check(tree_count == a ** (b - 1) * b ** (a - 1),
          ("tree total", a, b, tree_count))
    p = Fraction(a + b - 1, a * b)
    for i, count in enumerate(single):
        check(Fraction(count, tree_count) == p,
              ("edge marginal", a, b, i, count))
    for i, j in combinations(range(len(edges)), 2):
        u, v = edges[i]
        x, y = edges[j]
        transfer = (Fraction(int(u == x), b)
                    + Fraction(int(v == y), a)
                    - Fraction(1, a * b))
        check(Fraction(pair[(i, j)], tree_count) == p * p - transfer * transfer,
              ("pair inclusion", a, b, i, j))

    # Because the two sampled trees are independent, probabilities for edge
    # overlap and for two-edge overlap are squares of the tree inclusion rates.
    mean = Fraction(sum(c * c for c in single), tree_count ** 2)
    factorial_second = Fraction(2 * sum(c * c for c in pair.values()),
                                tree_count ** 2)
    variance = factorial_second + mean - mean * mean
    n = a + b
    expected = Fraction((n - 1) ** 2, a * b)
    predicted_variance = Fraction((a - 1) * (b - 1) * (n * n - 5 * n + 7),
                                  a * a * b * b)
    check(mean == expected, ("mean", a, b, mean, expected))
    check(variance == predicted_variance,
          ("variance", a, b, variance, predicted_variance))


for a in range(1, 5):
    for b in range(1, 5):
        enumerate_and_check(a, b)


def factor(a, b):
    return Fraction((a - 1) * (b - 1), a * a * b * b)


for n in range(4, 151):
    options = {a: factor(a, n - a) for a in range(2, n // 2 + 1)}
    maximum = max(options.values())
    maximizers = [a for a in options if options[a] == maximum]
    expected_maximizer = 3 if 6 <= n <= 9 else 2
    check(maximizers == [expected_maximizer],
          ("fixed-order variance maximum", n, maximizers))
    if n >= 10:
        seq = [options[a] for a in range(2, n // 2 + 1)]
        check(all(x > y for x, y in zip(seq, seq[1:])),
              ("strict monotonicity", n))

print(f"PASS: {assertions} exact assertions, independently enumerated tree counts and overlap moments")
