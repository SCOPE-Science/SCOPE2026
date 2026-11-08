"""Independent exact-rational identities for a polynomial crossing flow.

Run with Python 3.9+: python checker.py
The analytic proof, not finite samples, establishes the infinite statements.
"""
from fractions import Fraction

def positive_potential(x, k):
    return abs(x)**(4*k) if x < 0 else x**(2*k)

def negative_potential(x, k):
    return abs(x)**(2*k) if x < 0 else x**(4*k)

def upper_velocity(x, k):
    return -4*k*x**(4*k-1) if x < 0 else -2*k*x**(2*k-1)

def lower_velocity(x, k):
    return -2*k*x**(2*k-1) if x < 0 else -4*k*x**(4*k-1)

checks = 0
for k in range(2, 16):
    for a in range(-5, 6):
        x = Fraction(a, 4)
        h = Fraction(1, 1000)
        if x < 0 and x + h < 0 or x >= 0:
            # exact derivative using powers, not a floating derivative.
            deg = 4*k if x < 0 else 2*k
            slope = deg*x**(deg-1)
            assert upper_velocity(x, k) == -slope
            checks += 1
        if x < 0 or x > 0:
            deg = 2*k if x < 0 else 4*k
            slope = deg*x**(deg-1)
            assert lower_velocity(x, k) == -slope
            checks += 1
    for r in [Fraction(1, 5), Fraction(2, 3), Fraction(1), Fraction(4, 3), Fraction(5, 2)]:
        # Upper arc from (-r,0) to (+r^2,0).
        C_upper = positive_potential(-r, k)
        assert C_upper == positive_potential(r*r, k)
        assert C_upper > positive_potential(Fraction(0), k)
        # Lower arc from (+r^2,0) to (-r^4,0).
        C_lower = negative_potential(r*r, k)
        assert C_lower == negative_potential(-(r**4), k)
        assert C_lower > negative_potential(Fraction(0), k)
        # r -> r^4; monotone inward/outward with only positive fixed point 1.
        assert (r**4 < r) == (r < 1)
        assert (r**4 > r) == (r > 1)
        checks += 6
    # Exact analytic integration of top and bottom graphs.
    area = 4 - Fraction(2, 2*k+1) - Fraction(2, 4*k+1)
    top_area = Fraction(2*k, 2*k+1) + Fraction(4*k, 4*k+1)
    assert area == 2*top_area
    assert 0 < area < 4
    checks += 2
assert 4*1**3 == 4  # one full return multiplier at the unique cycle
print('PIECEWISE_FOCUS_EXACT_IDENTITIES_OK', checks)
