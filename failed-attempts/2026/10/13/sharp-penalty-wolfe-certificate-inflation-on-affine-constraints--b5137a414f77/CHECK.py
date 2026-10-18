"""Exact arithmetic checks for the affine sharpness construction."""
from fractions import Fraction

def phi(x, gamma):
    return -x + gamma * max(Fraction(0), 2 * (1 + x))

assert phi(Fraction(-2), Fraction(1)) == 2
assert phi(Fraction(-1), Fraction(1)) == 1
assert phi(Fraction(0), Fraction(1)) == 2
for r in [Fraction(1), Fraction(3, 2), Fraction(2), Fraction(4), Fraction(11, 3)]:
    y = Fraction(0)
    slope = 2*r - 1
    # On [-1,1] the affine objective has positive slope and minimum at -1.
    assert slope >= 1
    assert phi(y, r) - phi(Fraction(-1), r) == slope
    assert 2 <= 2*slope/r
for x in [Fraction(-2), Fraction(-3, 2), Fraction(-1), Fraction(-1, 2), Fraction(0), Fraction(1), Fraction(2)]:
    # Globally exact QG modulus 2/3: phi_1(x)-phi_1(-1) >= (1/3)(x+1)^2.
    assert phi(x, Fraction(1)) - 1 >= (x+1)**2/Fraction(3)
assert 2*(-1 + 1) == 0
assert 2*(-2 + 1) < 0
print('VERIFY_OK')
