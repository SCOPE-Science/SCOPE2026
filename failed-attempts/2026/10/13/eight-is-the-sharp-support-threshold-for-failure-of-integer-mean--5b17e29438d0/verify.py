"""Exact rational certificates for a finite-support log-concavity threshold.

Standard-library only.  Run: python verify.py
"""
from fractions import Fraction

WITNESSES = (
    (3, 1, 3, 2),
    (4, 1, 2, 3), (4, 2, 5, 3),
    (5, 1, 2, 3), (5, 2, 7, 6), (5, 3, 9, 5),
    (6, 1, 2, 3), (6, 2, 6, 7), (6, 3, 5, 4), (6, 4, 17, 9),
    (7, 1, 2, 3), (7, 2, 4, 5), (7, 3, 13, 12),
    (7, 4, 17, 13), (7, 5, 31, 16),
)

def H(n, m, q):
    return sum((i - m) * q**i for i in range(n))

def D(n, m, q):
    return sum(q**i for i in range(m + 1, n)) - sum(q**i for i in range(m + 1))

def Z(n, q):
    return sum(q**i for i in range(n))

def run():
    assert {(n, m) for (n, m, _, _) in WITNESSES} == {
        (n, m) for n in range(3, 8) for m in range(1, n - 1)
    }
    assert len(WITNESSES) == 15
    for n, m, numerator, denominator in WITNESSES:
        q = Fraction(numerator, denominator)
        h, d = H(n, m, q), D(n, m, q)
        assert h > 0 and d < 0, (n, m, q, h, d)
        assert H(n, m, q) / Z(n, q) == sum((i-m)*q**i for i in range(n)) / Z(n,q)
        assert D(n, m, q) / Z(n, q) == 2 * sum(q**i for i in range(m+1,n)) / Z(n,q) - 1
    low, high = Fraction(34,25), Fraction(11,8)
    assert H(8,5,low) == Fraction(-5507579937,6103515625)
    assert H(8,5,high) == Fraction(416103,1048576)
    assert D(8,5,low) == Fraction(819586169,6103515625)
    assert D(8,5,high) == Fraction(1458763,2097152)
    assert H(8,5,low) < 0 < H(8,5,high)
    assert D(8,5,low) > 0
    print('PASS: 15 exhaustive rational witnesses for support lengths 3..7')
    print('PASS: eight-point mean-root bracket and strict majority counterexample')

if __name__ == '__main__':
    run()
