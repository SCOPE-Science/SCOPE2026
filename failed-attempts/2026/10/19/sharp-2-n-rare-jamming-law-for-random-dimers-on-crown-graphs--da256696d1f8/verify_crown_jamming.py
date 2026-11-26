"""Independent finite-size checks of greedy dimer jamming on crown graphs.

Run with Python 3 standard library: python verify_crown_jamming.py.
The tests do not substitute for the analytic all-size proof.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import permutations


def reduced_failure(n):
    @lru_cache(None)
    def f(k, t):
        if k == 1:
            return Fraction(int(t == 1))
        den = k * k - t
        return (Fraction(t * (t - 1), den) * f(k - 1, t - 2) if t >= 2 else 0) + (Fraction(2 * t * (k - t), den) * f(k - 1, t - 1) if t >= 1 else 0) + (Fraction((k - t) ** 2, den) * f(k - 1, t) if k > t else 0)
    return f(n, n)


def independent_graph_failure(n):
    @lru_cache(None)
    def f(a, b):
        edges = [(i, j) for i in range(n) for j in range(n)
                 if i != j and ((a >> i) & 1) and ((b >> j) & 1)]
        if not edges:
            return Fraction(int(a != 0 or b != 0))
        return sum((f(a & ~(1 << i), b & ~(1 << j)) for i, j in edges), Fraction()) / len(edges)
    return f((1 << n) - 1, (1 << n) - 1)


def edge_order_failure(n):
    edges = [(i, j) for i in range(n) for j in range(n) if i != j]
    misses = 0
    total = 0
    for order in permutations(edges):
        left = right = 0
        for i, j in order:
            if not (left & (1 << i)) and not (right & (1 << j)):
                left |= 1 << i
                right |= 1 << j
        misses += (left != (1 << n) - 1)
        total += 1
    return Fraction(misses, total)


def harmonic(k):
    return sum((Fraction(1, j) for j in range(1, k + 1)), Fraction())


def moment_checks(n):
    pr = {n: Fraction(1)}
    for k in range(n, 0, -1):
        total = sum(pr.values(), Fraction())
        assert total == 1, (n, k, 'normalization')
        second = sum((t * (t - 1) * p for t, p in pr.items()), Fraction())
        assert second <= Fraction(k * k * (k * k - 1), n * (n + 1)), (n, k, 'moment')
        if k == 1:
            assert pr.get(1, 0) == reduced_failure(n)
            break
        nxt = {}
        for t, p in pr.items():
            den = k * k - t
            for tt, num in ((t-2, t * (t-1)), (t-1, 2*t*(k-t)), (t, (k-t)**2)):
                if num:
                    nxt[tt] = nxt.get(tt, Fraction()) + p * Fraction(num, den)
        pr = nxt


def main():
    for n in range(2, 8):
        a = reduced_failure(n)
        b = independent_graph_failure(n)
        assert a == b, (n, a, b)
    assert edge_order_failure(3) == reduced_failure(3) == Fraction(1, 3)
    for n in range(2, 18):
        a = reduced_failure(n)
        low = Fraction(2, n+1) - Fraction(4, n*(n+1)) * harmonic(n-1)
        high = Fraction(2, n+1)
        assert low <= a <= high, (n, low, a, high)
        moment_checks(n)
    print('PASS: 6 independent graph-state rational comparisons, complete 720-order check, 16 exact bound and factorial-moment checks.')
    for n in (3, 4, 5, 10, 16):
        print('n=', n, 'p_failure=', reduced_failure(n))


if __name__ == '__main__':
    main()
