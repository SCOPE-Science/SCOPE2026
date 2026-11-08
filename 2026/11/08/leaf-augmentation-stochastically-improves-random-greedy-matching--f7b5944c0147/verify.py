"""Exact tests of random-order greedy matchings on pendant-decorated paths.

Uses only the Python standard library. Run: python verify.py
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import permutations
import math
import random


def convolve(a, b):
    c = Counter()
    for i, x in a.items():
        for j, y in b.items():
            c[i + j] += x * y
    return c


@lru_cache(None)
def distribution(n, q):
    if n == 0:
        return {0: Fraction(1)}
    assert n >= 1 and q >= 1
    m = (q + 1) * n - 1
    total = Counter()
    for i in range(n):
        for k, v in convolve(distribution(i, q), distribution(n - i - 1, q)).items():
            total[k + 1] += q * v / m
    for i in range(n - 1):
        for k, v in convolve(distribution(i, q), distribution(n - i - 2, q)).items():
            total[k + 1] += v / m
    return dict(total)


def core_edges(n, kind="path"):
    if kind == "path":
        return [(i, i + 1) for i in range(n - 1)]
    if kind == "complete":
        return [(i, j) for i in range(n) for j in range(i + 1, n)]
    raise ValueError(kind)


def edges_of_decorated(n, q, core):
    result = [(u, v, True) for u, v in core]
    result += [(i, n + i * q + j, False) for i in range(n) for j in range(q)]
    return result


def evaluate_order(edges):
    used = set()
    picked = 0
    core_count = 0
    for a, b, is_core in edges:
        if a not in used and b not in used:
            used.add(a)
            used.add(b)
            picked += 1
            core_count += is_core
    return picked, core_count


def exact_order_distribution(n, q):
    edges = edges_of_decorated(n, q, core_edges(n))
    counts = Counter()
    for ordering in permutations(edges):
        picked, _ = evaluate_order(ordering)
        counts[picked] += 1
    fac = math.factorial(len(edges))
    return {k: Fraction(v, fac) for k, v in counts.items()}


def stochastic_geq(b, a):
    return all(sum(v for k, v in b.items() if k >= j) >=
               sum(v for k, v in a.items() if k >= j)
               for j in range(max(max(a), max(b)) + 2))


def run():
    checks = 0
    for n, q in [(1, 1), (1, 3), (2, 1), (2, 3),
                 (3, 1), (3, 2), (4, 1), (5, 1)]:
        rec = distribution(n, q)
        brute = exact_order_distribution(n, q)
        assert rec == brute, (n, q, rec, brute)
        checks += 1
    for n in range(1, 19):
        for q in range(1, 9):
            p = distribution(n, q)
            assert sum(p.values()) == 1
            assert set(p) == set(range((n + 1) // 2, n + 1))
            checks += 2
            r = distribution(n, q + 1)
            assert stochastic_geq(r, p)
            checks += 1
            if n >= 2:
                assert r != p
                checks += 1
    # Exhaustively check pathwise comparison when attaching one new leaf
    # to a single root in small core graphs, with arbitrary old edge orders.
    for n, core in [(2, core_edges(2)), (3, core_edges(3)),
                    (3, core_edges(3, "complete")), (4, core_edges(4))]:
        old = edges_of_decorated(n, 1, core)
        for v in range(n):
            extra = (v, 2 * n + v, False)
            for order in permutations(old + [extra]):
                old_order = tuple(e for e in order if e != extra)
                old_size, old_core = evaluate_order(old_order)
                new_size, new_core = evaluate_order(order)
                assert old_core >= new_core
                assert old_size == n - old_core
                assert new_size == n - new_core
                checks += 3
    rng = random.Random(1729)
    for n in range(3, 12):
        for trial in range(500):
            c = [(i, j) for i in range(n) for j in range(i + 1, n)
                 if rng.randrange(4) == 0]
            old = edges_of_decorated(n, 1, c)
            extra = (rng.randrange(n), n * 2 + trial, False)
            # Use an isolated fresh leaf ID, disjoint from every existing vertex.
            extra = (extra[0], 2 * n + trial + 1, False)
            if extra[1] < 2 * n:
                raise AssertionError("leaf ID collision")
            order = old + [extra]
            rng.shuffle(order)
            old_order = [e for e in order if e != extra]
            _, d0 = evaluate_order(old_order)
            _, d1 = evaluate_order(order)
            assert d1 <= d0
            checks += 1
    # Check coefficients of the Riccati identity independently of the
    # recurrence's specific index convention.
    for q in range(1, 8):
        N = 20
        F = [distribution(n, q) for n in range(N + 1)]
        for n in range(1, N + 1):
            lhs = Counter({k: Fraction(((q + 1) * n - 1)) * v
                           for k, v in F[n].items()})
            rhs = Counter()
            for i in range(n):
                for k, v in convolve(F[i], F[n - 1 - i]).items():
                    rhs[k + 1] += q * v
            for i in range(n - 1):
                for k, v in convolve(F[i], F[n - 2 - i]).items():
                    rhs[k + 1] += v
            assert dict(lhs) == dict(rhs)
            checks += 1
    print(f"VERIFY_OK {checks} exact and seeded checks")


if __name__ == "__main__":
    run()
