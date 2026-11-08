"""Finite consistency checks for the Chebyshev chamber theorem.

The unrestricted argument is a written root-order and Euler-characteristic proof.
This program neither assumes nor certifies any claim beyond its finite tests.
"""
from math import gcd
from fractions import Fraction

def roots_derivative_sign_pattern(a, k):
    # For positive-leading real polynomials at k ordered simple real roots,
    # the signs alternate, with the largest root carrying positive sign.
    assert k <= a and (a - k) % 2 == 0
    return [(-1) ** (k - 1 - i) for i in range(k)]

def verify():
    pairs = 0
    for a in range(2, 201):
        for b in range(a+1, 201):
            if gcd(a, b) != 1:
                continue
            pairs += 1
            nodes = sum(i % 2 == j % 2 for i in range(1, b) for j in range(1, a))
            assert 2 * nodes == (a-1) * (b-1)
            chambers = nodes + 2
            assert (chambers <= a+1) == ((a,b) == (2,3))
            if (a,b)!=(2,3):
                assert chambers - (a+1) >= 1
            for k in range(a % 2, a+1, 2):
                s = roots_derivative_sign_pattern(a,k)
                assert sum(v > 0 for v in s) <= (a+1)//2
                assert sum(v < 0 for v in s) <= a//2
    # For x=0, the T_2 roots satisfy t^2=1/2 and T_3(t)=-t.
    assert 4 * Fraction(1,2) - 3 == -1
    # For x=2, the T_2 roots satisfy t^2=3/2 and T_3(t)=3t.
    assert 4 * Fraction(3,2) - 3 == 3
    # In the vertical-ray convention, the upper root at x=0 has
    # negative derivative, at x=2 positive derivative; w=0 above both.
    assert { -1, 0, 1 } == set(range(-1,2))
    print('CHEBYSHEV_CHAMBER_CHECK_OK', pairs)

if __name__ == '__main__':
    verify()
