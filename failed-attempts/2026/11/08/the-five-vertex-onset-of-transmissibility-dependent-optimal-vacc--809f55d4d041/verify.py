#!/usr/bin/env python3
"""Exact finite-graph proof checker for one-vertex SIR bond-percolation protection.

Requires Python >= 3.9; standard library only. Executing this file prints PASS.
The certificate covers every labeled connected simple graph of orders 2--5.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from math import comb

DEGREE = 6  # after one vertex is removed from a graph of at most five vertices
FIRST = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 4))
SECOND = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 4), (3, 4))


def multiply(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def power(a, n):
    result = [1]
    for _ in range(n):
        result = multiply(result, a)
    return result


def bernstein_certificate(coeff, left_numerator, right_numerator):
    """Coefficients of 4^6(1+z)^6 f((L+Rz)/(4(1+z))).

    All nonnegative coefficients imply f(p)>=0 for L/4<=p<=R/4;
    a nonzero positive coefficient implies strict inequality inside.
    """
    out = [0] * (DEGREE + 1)
    for k, ck in enumerate(coeff):
        if ck == 0:
            continue
        term = multiply(power([left_numerator, right_numerator], k),
                        power([1, 1], DEGREE - k))
        for j, value in enumerate(term):
            out[j] += ck * (4 ** (DEGREE - k)) * value
    return tuple(out)


def connected(n, edges):
    seen = {0}
    old_size = -1
    while len(seen) != old_size:
        old_size = len(seen)
        for a, b in edges:
            if a in seen:
                seen.add(b)
            if b in seen:
                seen.add(a)
    return len(seen) == n


def component_square_count(n, edges):
    parent = list(range(n))
    def root(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for a, b in edges:
        a, b = root(a), root(b)
        if a != b:
            parent[a] = b
    sizes = Counter(root(v) for v in range(n))
    # Independent pair-count formulation checks the component-square identity.
    value = sum(s * s for s in sizes.values())
    other = sum(1 for i in range(n) for j in range(n) if root(i) == root(j))
    assert value == other
    return value


def polynomial(n, edges, deleted):
    survivors = [v for v in range(n) if v != deleted]
    mapping = {v: i for i, v in enumerate(survivors)}
    remaining = [(mapping[a], mapping[b]) for a, b in edges
                 if a != deleted and b != deleted]
    m = len(remaining)
    assert m <= DEGREE
    coefficients = [0] * (DEGREE + 1)
    for mask in range(1 << m):
        retained = [edge for j, edge in enumerate(remaining) if (mask >> j) & 1]
        square_sum = component_square_count(n - 1, retained)
        k = mask.bit_count()
        for j in range(m - k + 1):
            coefficients[k + j] += square_sum * (-1) ** j * comb(m - k, j)
    return tuple(coefficients)


def evaluate(coefficients, x):
    return sum(c * x ** k for k, c in enumerate(coefficients))


def canonical_form(n, edges):
    return min(tuple(sorted(tuple(sorted((perm[a], perm[b]))) for a, b in edges))
               for perm in permutations(range(n)))


def optimizers(polynomials, x):
    values = [evaluate(poly, x) for poly in polynomials]
    optimum = min(values)
    return tuple(v for v, value in enumerate(values) if value == optimum)


def main():
    counts = Counter()
    exceptions = Counter()
    strict_comparisons = 0
    all_labeled_graphs = 0
    for n in range(2, 6):
        possible = list(combinations(range(n), 2))
        for edge_mask in range(1 << len(possible)):
            all_labeled_graphs += 1
            edges = tuple(edge for j, edge in enumerate(possible) if (edge_mask >> j) & 1)
            if not connected(n, edges):
                continue
            counts[n] += 1
            costs = [polynomial(n, edges, v) for v in range(n)]
            low = optimizers(costs, Fraction(1, 8))
            high = optimizers(costs, Fraction(1, 2))
            middle = optimizers(costs, Fraction(1, 4))
            assert middle == tuple(sorted(set(low) | set(high)))
            for chosen, alpha, beta in ((low, 0, 1), (high, 1, 4)):
                for u in chosen:
                    for v in chosen:
                        assert costs[u] == costs[v]
                    for w in range(n):
                        difference = tuple(costs[w][i] - costs[u][i]
                                           for i in range(DEGREE + 1))
                        cert = bernstein_certificate(difference, alpha, beta)
                        assert all(x >= 0 for x in cert), (n, edges, u, w, cert)
                        if w not in chosen:
                            assert any(x > 0 for x in cert)
                            strict_comparisons += 1
            if low != high:
                assert n == 5
                form = canonical_form(n, edges)
                assert form in (FIRST, SECOND), (n, edges, form)
                exceptions[form] += 1
    assert all_labeled_graphs == 2 + 8 + 64 + 1024
    assert counts == Counter({2: 1, 3: 4, 4: 38, 5: 728})
    assert exceptions == Counter({FIRST: 60, SECOND: 30})

    first_costs = [polynomial(5, FIRST, v) for v in range(5)]
    second_costs = [polynomial(5, SECOND, v) for v in range(5)]
    assert first_costs[0] == first_costs[1] == (4, 6, 4, 2, 0, 0, 0)
    assert first_costs[2] == (4, 6, 6, -6, 0, 0, 0)
    assert second_costs[0] == second_costs[1] == (4, 8, 8, 8, -12, 0, 0)
    assert second_costs[2] == second_costs[3] == (4, 8, 10, -2, -4, 0, 0)
    assert tuple(first_costs[2][i] - first_costs[0][i]
                 for i in range(7)) == (0, 0, 2, -8, 0, 0, 0)
    assert tuple(second_costs[2][i] - second_costs[0][i]
                 for i in range(7)) == (0, 0, 2, -10, 8, 0, 0)

    for x, low_first, low_second in ((Fraction(1, 8), (0, 1), (0, 1)),
                                      (Fraction(1, 4), (0, 1, 2), (0, 1, 2, 3)),
                                      (Fraction(1, 2), (2,), (2, 3)),
                                      (Fraction(1), (2,), (0, 1, 2, 3, 4))):
        assert optimizers(first_costs, x) == low_first
        assert optimizers(second_costs, x) == low_second
    print('PASS: exact exhaustive connected labeled graph counts:', dict(counts))
    print('PASS: only switching isomorphism classes:', len(exceptions))
    print('PASS: labeled switching instances: 60 and 30')
    print('PASS: nonnegative integer Bernstein certificates and strict comparisons:', strict_comparisons)
    print('PASS: both transitions occur at p=1/4, with the specified optimal sets')


if __name__ == '__main__':
    main()
