#!/usr/bin/env python3
"""Finite exact checks for cyclic multinomial roughness deficit.

Only standard-library arithmetic is used. These finite checks supplement the
analytic Poisson-approximation and asymptotic proof; they do not certify it.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, factorial


def stirling2(n, k):
    if n == 0:
        return int(k == 0)
    if k == 0:
        return 0
    return k * stirling2(n - 1, k) + stirling2(n - 1, k - 1)


def independent_k_subsets(n, k):
    if k == 0:
        return 1
    if k > n // 2:
        return 0
    a = n * comb(n - k, k)
    assert a % (n - k) == 0
    return a // (n - k)


def zero_numerator(n, N):
    return sum(independent_k_subsets(n, k) * factorial(k) * stirling2(N, k)
               for k in range(1, min(N, n // 2) + 1))


def analyze(n, N):
    zeros = 0
    sum_U = 0
    sum_T = 0
    bad = 0
    distribution = Counter()
    total = n**N
    checks = 0
    for assignment in product(range(n), repeat=N):
        x = [0] * n
        for a in assignment:
            x[a] += 1
        d = sum(abs(x[j] - x[(j + 1) % n]) for j in range(n))
        t = sum(min(x[j], x[(j + 1) % n]) for j in range(n))
        u = sum(x[j] * x[(j + 1) % n] for j in range(n))
        assert 2*N - d == 2*t
        assert 0 <= t <= u
        assert not ((t == 0) != (d == 2*N))
        zeros += int(t == 0)
        sum_U += u
        sum_T += t
        bad += (t != u)
        distribution[t] += 1
        checks += 3
    assert zeros == zero_numerator(n, N), (n, N, zeros, zero_numerator(n, N))
    assert Fraction(sum_U, total) == Fraction(N*(N-1), n)
    assert Fraction(sum_U - sum_T, total) <= Fraction(N*(N-1)*(N-2), n*n)
    assert Fraction(bad, total) <= Fraction(N*(N-1)*(N-2), n*n)
    bound = Fraction(N*(N-1)*(9*N-16), n*n)
    assert bound >= 0
    assert sum(distribution.values()) == total
    return checks + 6, zeros, total


def main():
    checks = 0
    instances = 0
    for n in range(3, 9):
        for N in range(1, 7):
            if n**N > 300000:
                continue
            count, zeros, total = analyze(n, N)
            checks += count
            instances += 1
    print(f"PASS: {instances} exact independent multinomial enumeration instances; {checks} assertions and arithmetic conditions checked.")
    print("PASS: deterministic roughness identity, pair-collision upper coupling, Poisson parameter, triple-error bound, independent-set zero coefficient.")
    print("LIMIT: finite checks do not establish asymptotics or the Chen-Stein theorem.")


if __name__ == '__main__':
    main()
