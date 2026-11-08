"""Exact finite checks for cross-record indicator covariance in uniform permutations.

Run: python verify.py
This is an auxiliary finite check, not a replacement for the all-n proof.
"""
from fractions import Fraction
from itertools import permutations
from math import comb, factorial


def counts(n):
    joint = [[0] * n for _ in range(n)]
    for p in permutations(range(1, n+1)):
        pos = [0] * (n+1)
        for ix, value in enumerate(p, start=1):
            pos[value] = ix
        a = [False] * n
        b = [False] * n
        record = 0
        for ix, value in enumerate(p):
            a[ix] = value > record
            record = max(record, value)
        record = 0
        for ix in range(n):
            value = pos[ix+1]
            b[ix] = value > record
            record = max(record, value)
        active_b = [ix for ix, yes in enumerate(b) if yes]
        for ix, yes in enumerate(a):
            if yes:
                for jx in active_b:
                    joint[ix][jx] += 1
    return joint


def expected_joint(n, i, j):
    # Here i,j are one-based.
    value = Fraction(1, i*j)
    if i == j:
        value += Fraction(i-1, i*i*comb(n,i))
    return value


def run_checks():
    assertions = 0
    for n in range(2, 10):
        joint = counts(n)
        for i in range(1, n+1):
            for j in range(1, n+1):
                assert Fraction(joint[i-1][j-1], factorial(n)) == expected_joint(n,i,j), (n,i,j)
                assertions += 1
        # Exact global covariance: sum of the diagonal only.
        actual = sum(Fraction(joint[i-1][j-1], factorial(n)) - Fraction(1, i*j)
                     for i in range(1,n+1) for j in range(1,n+1))
        theorem = sum(Fraction(i-1, i*i*comb(n,i)) for i in range(2,n+1))
        assert actual == theorem
        assertions += 1
    print('PASS: all exact joint probabilities for n=2,...,9')
    print(f'PASS: {assertions} assertions; no floating-point arithmetic')
    print('Limits: finite enumeration does not prove the universal formula or asymptotic.')

if __name__ == '__main__':
    run_checks()
