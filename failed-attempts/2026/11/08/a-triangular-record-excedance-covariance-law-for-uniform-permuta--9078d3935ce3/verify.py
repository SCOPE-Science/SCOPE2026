"""Exact finite checks of the record--excedance covariance identities.

The derivation for arbitrary n is analytic. This checker verifies small
permutation spaces and algebraic consequences, not the infinite theorem.
"""
from itertools import permutations
from fractions import Fraction
from math import comb, factorial


def predicted(n, i, j):
    if j > i:
        return Fraction(0)
    if j == i:
        return Fraction(1, n) - Fraction(1, i * comb(n, i))
    return -Fraction(j, n * i * (i - 1))


def global_covariance(n):
    return Fraction(n - 1, 2 * n) - sum(
        (Fraction(1, i * comb(n, i)) for i in range(2, n + 1)),
        Fraction(0),
    )


def exact_exhaustive(n):
    total = factorial(n)
    records = [0] * n
    excedances = [0] * n
    joint = [[0] * n for _ in range(n)]
    rsum = esum = resum = 0
    for p in permutations(range(1, n + 1)):
        rec = []
        high = 0
        exc = []
        for i, v in enumerate(p, start=1):
            if v > high:
                high = v
                rec.append(i - 1)
            if v > i:
                exc.append(i - 1)
        for i in rec:
            records[i] += 1
        for j in exc:
            excedances[j] += 1
        for i in rec:
            for j in exc:
                joint[i][j] += 1
        rsum += len(rec)
        esum += len(exc)
        resum += len(rec) * len(exc)
    checks = 0
    for i in range(1, n + 1):
        assert Fraction(records[i - 1], total) == Fraction(1, i)
        checks += 1
        for j in range(1, n + 1):
            observed = Fraction(joint[i - 1][j - 1], total) - (
                Fraction(records[i - 1] * excedances[j - 1], total * total)
            )
            assert observed == predicted(n, i, j), (n, i, j, observed, predicted(n, i, j))
            checks += 1
    assert Fraction(resum, total) - Fraction(rsum * esum, total * total) == global_covariance(n)
    checks += 1
    return total, checks


def main():
    check_total = 0
    for n in range(2, 9):
        total, checks = exact_exhaustive(n)
        check_total += checks
        print(f"n={n}: {total} permutations, {checks} exact checks")
    for n in range(2, 101):
        assert sum((predicted(n, i, j) for i in range(1, n + 1) for j in range(1, n + 1)), Fraction(0)) == global_covariance(n)
        assert (global_covariance(n) < 0) == (n <= 4)
        assert (global_covariance(n) > 0) == (n >= 5)
        if n >= 3:
            assert global_covariance(n) > global_covariance(n - 1)
        check_total += 4 if n >= 3 else 3
    print(f"PASS: {check_total} exact checks; analytic proof needed for all n")


if __name__ == '__main__':
    main()
