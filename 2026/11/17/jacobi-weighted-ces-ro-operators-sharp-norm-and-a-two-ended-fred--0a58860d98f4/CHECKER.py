"""Finite diagnostics for the Jacobi-weighted Cesaro spectral identities.

These tests do not replace the analytic infinite-dimensional proof.
Run: python CHECKER.py
"""
from fractions import Fraction as F
import math


def parameters(p, gamma, delta):
    assert p > 1 and gamma < p - 1 and delta > -1
    return (p - 1 - gamma) / p, (delta + 1) / p


def check():
    count = 0
    cases = [
        (F(2), F(0), F(0)),
        (F(3), F(0), F(0)),
        (F(3, 2), F(0), F(0)),
        (F(2), F(2, 5), F(4, 5)),
        (F(2), F(-2, 5), F(-4, 5)),
        (F(5, 2), F(-3, 4), F(1, 3)),
        (F(7, 4), F(1, 3), F(2, 5)),
    ]
    for p, gamma, delta in cases:
        A, B = parameters(p, gamma, delta)
        assert A > 0 and B > 0; count += 1
        assert p * A == p - 1 - gamma and p * B == delta + 1; count += 1
        assert (A < B) == (p < gamma + delta + 2); count += 1
        assert (A > B) == (p > gamma + delta + 2); count += 1
        assert (A == B) == (p == gamma + delta + 2); count += 1
        assert F(1) / min(A, B) == max(F(1)/A, F(1)/B); count += 1
        if A < B:
            theta = (A+B)/2
            # Beta exponents of the exact eigenfunction's p-th norm.
            assert p*(theta-A) > 0 and p*(B-theta) > 0; count += 1
            # The eigenfunction's two endpoint power exponents exceed -1.
            left_exp = p*(theta-1) + gamma
            right_exp = delta - p*theta
            assert left_exp > -1 and right_exp > -1; count += 1
        if B < A:
            theta = (A+B)/2
            # The annihilator is a bounded dual functional precisely here.
            assert A-theta > 0 and theta-B > 0; count += 1
        for y in (-8., -3., -0.5, 0., 0.5, 3., 8.):
            x = 1.0/(1.0+math.exp(-y))
            v = math.exp(-float(A)*y)*(1.+math.exp(y))**float(A-B)
            v2 = x**((float(gamma)+1.-float(p))/float(p)) * (1.-x)**((float(delta)+1.)/float(p))
            assert abs(v/v2-1)<1e-12; count += 1
            # The transformed derivative has limiting decay A and B.
            deriv_log_v = -float(A)+(float(A)-float(B))*x
            assert abs(deriv_log_v - (-float(A)*(1-x)-float(B)*x))<1e-12; count += 1
        for t in (0.1,0.5,2.0,5.0):
            # The positive translation norm is the sharp endpoint exponent.
            ratios=[]
            for s in (-100., -10., 0., 10., 100.):
                v_rat = -float(A)*t + float(A-B)*(math.log1p(math.exp(s+t)) - math.log1p(math.exp(s))) if s+t<500 else None
                if v_rat is not None: ratios.append(math.exp(v_rat))
            assert all(r <= math.exp(-float(min(A,B))*t)*(1+1e-12) for r in ratios); count += 1
    # The unweighted specializations reproduce the two reciprocal exponents.
    for p in (F(3, 2), F(2), F(3), F(5)):
        A,B=parameters(p,F(0),F(0))
        assert A==1-1/p and B==1/p; count+=1
    print(f"{count} finite symbolic and numerical diagnostic assertions passed")


if __name__ == '__main__':
    check()
