#!/usr/bin/env python3
"""Exact exhaustive tests for edge-length enumerators of complete-graph matching polytopes.

Requires Python 3.9+.  Adjacency is tested by connectivity of symmetric differences,
independently of the alternating-path count used for the formula.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb, factorial, exp


def all_matchings(vertices):
    if not vertices:
        yield frozenset()
        return
    head, tail = vertices[0], vertices[1:]
    yield from all_matchings(tail)
    for other in tail:
        rest = [v for v in tail if v != other]
        edge = (min(head, other), max(head, other))
        for smaller in all_matchings(rest):
            yield smaller.union([edge])


def connected_difference(a, b):
    edges = a.symmetric_difference(b)
    if not edges:
        return False
    unseen = {v for edge in edges for v in edge}
    stack = [next(iter(unseen))]
    unseen.remove(stack[0])
    while stack:
        v = stack.pop()
        for x, y in edges:
            if x == v and y in unseen:
                unseen.remove(y)
                stack.append(y)
            elif y == v and x in unseen:
                unseen.remove(x)
                stack.append(x)
    return not unseen


def predicted(n, k):
    assert n >= 2 and 0 <= k <= n // 2
    s = n - 2*k
    result = Counter()
    for j in range(1, k+1):
        c = comb(k, j)*factorial(j)
        result[2*j - 1] += c*2**(j-1)
        result[2*j] += s*c*2**j
        if j >= 2:
            result[2*j] += comb(k, j)*factorial(j-1)*2**(j-1)
    for j in range(0, k+1):
        result[2*j + 1] += comb(s, 2)*comb(k, j)*factorial(j)*2**j
    return +result


def direct(n, k, matchings):
    base = next(m for m in matchings if len(m) == k)
    lengths = Counter()
    for m in matchings:
        if connected_difference(base, m):
            lengths[len(base.symmetric_difference(m))] += 1
    return lengths


def main():
    tests = 0
    for n in range(2, 11):
        matchings = list(all_matchings(list(range(n))))
        for k in range(n//2 + 1):
            observed, claimed = direct(n, k, matchings), predicted(n, k)
            assert observed == claimed, (n, k, observed, claimed)
            tests += 1

    # Exact checks of conditional probability masses and a finite-size approach
    # to the Poisson/three-path-type limit.  No finite check is used as a proof.
    for s in range(5):
        weights = [1, 2*s, s*(s-1)]
        normalizer = s*s+s+1
        assert sum(weights) == normalizer
        for k in (20, 50, 100):
            h = predicted(2*k+s, k)
            degree = sum(h.values())
            ak = 2**(k-1)*factorial(k)
            ratio = Fraction(degree, normalizer*ak)
            assert abs(float(ratio) - exp(0.5)) < 0.2
        # The Poisson weights are exact consequences of A_{k-r}/A_k.
        for r in range(6):
            k = 20
            aj = comb(k, k-r)*factorial(k-r)*2**(k-r-1)
            ak = 2**(k-1)*factorial(k)
            assert Fraction(aj, ak) == Fraction(1, 2**r*factorial(r))

    print(f'KCOMPLETE_MATCHING_EDGE_METRIC_PASS ({tests} exhaustive strata, 15 asymptotic diagnostics)')

if __name__ == '__main__':
    main()
