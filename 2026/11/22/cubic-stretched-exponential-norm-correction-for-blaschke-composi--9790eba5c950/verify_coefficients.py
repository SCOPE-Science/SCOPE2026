"""Supplementary exact-rational checks for the analytic cubic boundary jet.

Run: python3 verify_coefficients.py
No dependencies outside Python's standard library. The general infinite-dimensional
statement follows from the proof, not from these finite calculations.
"""
from fractions import Fraction as Q
from math import comb


def jet(lambda_):
    """Taylor coefficients through degree three of b(exp(s/2)) and F=2log b."""
    a = [Q(1), Q(1, 2), Q(1, 8), Q(1, 48)]
    numerator = [a[0] - lambda_] + a[1:]
    denominator = [Q(1) - lambda_] + [-lambda_ * v for v in a[1:]]
    b = []
    for k in range(4):
        b.append((numerator[k] - sum(denominator[j] * b[k-j]
                  for j in range(1, k+1))) / denominator[0])
    assert b[0] == 1
    return 2*b[1], 2*(b[2]-b[1]**2/2), 2*(b[3]-b[1]*b[2]+b[1]**3/3)


def coef(lambda_, n, k):
    return sum(Q(comb(n, j)) * (-lambda_)**(n-j) *
               Q(comb(n+k-j-1, k-j)) * lambda_**(k-j)
               for j in range(min(k, n)+1))


def main():
    count = 0
    for lam in [Q(1, 10), Q(1, 5), Q(1, 3), Q(1, 2), Q(2, 3), Q(4, 5)]:
        u = (1+lam)/(1-lam)
        cubic = lam*(1+lam)/(12*(1-lam)**3)
        f1, f2, f3 = jet(lam)
        assert f1 == u and f2 == 0 and f3 == cubic
        assert cubic == u*(u*u-1)/48
        count += 4
        for n in range(1, 7):
            # The constant and first coefficient are directly known.
            assert coef(lam, n, 0) == (-lam)**n
            assert coef(lam, n, 1) == n*(-lam)**(n-1)*(1-lam*lam)
            count += 2
    print(f"PASS: {count} exact rational coefficient identities")


if __name__ == "__main__":
    main()
