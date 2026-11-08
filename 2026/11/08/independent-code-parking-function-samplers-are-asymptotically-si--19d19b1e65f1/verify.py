"""Finite exact checks for independent inversion-code parking samplers.

Run with Python 3: python verify.py
This verifies combinatorial identities and small cases; asymptotic singularity
uses the analytic Chebyshev/Brownian-excursion argument in RESULT.md.
"""
from fractions import Fraction as F
from itertools import permutations, product
from collections import defaultdict
from math import factorial


def is_parking(seq):
    counts = [0] * (len(seq) + 1)
    for a in seq:
        counts[a] += 1
    cumulative = 0
    for k in range(1, len(seq) + 1):
        cumulative += counts[k]
        if cumulative < k:
            return False
    return True


def mallows_code(perm):
    pos = {v: p for p, v in enumerate(perm)}
    n = len(perm)
    return tuple(1 + sum(pos[j] < pos[i] for i in range(1, j)) for j in range(1, n + 1))


def direct_surplus(n, q):
    """Direct Mallows-permutation enumeration; shuffling does not change surplus."""
    k = n // 2
    num = defaultdict(F)
    den = F(0)
    cases = 0
    for perm in permutations(range(1, n + 1)):
        code = mallows_code(perm)
        inversion_count = sum(x - 1 for x in code)
        w = q ** inversion_count
        excess = sum(x <= k for x in code) - k
        assert excess >= 0
        num[excess] += w
        den += w
        cases += 1
    assert cases == factorial(n)
    return {a: v / den for a, v in num.items()}


def bernoulli_surplus(n, q):
    k = n // 2
    pmf = [F(1)]
    mean = F(0)
    variance = F(0)
    for j in range(k + 1, n + 1):
        numerator = sum((q ** r for r in range(k)), F(0))
        denominator = sum((q ** r for r in range(j)), F(0))
        p = numerator / denominator
        assert 0 <= p <= 1
        mean += p
        variance += p * (1 - p)
        new = [F(0)] * (len(pmf) + 1)
        for i, a in enumerate(pmf):
            new[i] += a * (1 - p)
            new[i + 1] += a * p
        pmf = new
    assert sum(pmf) == 1
    observed_mean = sum((F(i) * x for i, x in enumerate(pmf)), F(0))
    observed_var = sum(((F(i) - mean) ** 2 * x for i, x in enumerate(pmf)), F(0))
    assert mean == observed_mean
    assert variance == observed_var
    assert variance <= mean
    return {i: x for i, x in enumerate(pmf) if x}, mean, variance


def exact_uniform_pmf(n):
    k = n // 2
    counts = defaultdict(int)
    total = 0
    for a in product(range(1, n + 1), repeat=n):
        if is_parking(a):
            e = sum(x <= k for x in a) - k
            assert e >= 0
            counts[e] += 1
            total += 1
    assert total == (n + 1) ** (n - 1), (n, total)
    return {i: F(v, total) for i, v in counts.items()}


def tv(p, r):
    return sum((abs(p.get(x, F(0)) - r.get(x, F(0))) for x in set(p) | set(r)), F(0)) / 2


def run():
    checks = 0
    for n in range(2, 7):
        u = exact_uniform_pmf(n)
        assert sum(u.values()) == 1
        checks += 2
        for q in (F(1, 2), F(1), F(3, 2), F(2)):
            direct = direct_surplus(n, q)
            predicted, m, var = bernoulli_surplus(n, q)
            assert direct == predicted, (n, q, direct, predicted)
            checks += 1
            for k in set(direct) | set(predicted):
                assert direct.get(k, F(0)) == predicted.get(k, F(0))
                checks += 1
            z = tv(direct, u)
            assert 0 <= z <= 1
            checks += 1
            print(f'n={n} q={str(q)}: E[S]={m}, Var[S]={var}, TV(surplus)={float(z):.8f}')
    # Independent factorial codes always satisfy the parking inequalities.
    for n in range(2, 7):
        for code in product(*(range(1, j + 1) for j in range(1, n + 1))):
            assert is_parking(code)
            checks += 1
    print('PASS: exact finite checks =', checks)


if __name__ == '__main__':
    run()
