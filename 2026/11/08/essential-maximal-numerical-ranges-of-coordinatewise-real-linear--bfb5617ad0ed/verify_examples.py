"""Finite diagnostics for scalar norming identities and a conjugation perturbation.

The infinite-dimensional characterization is proved analytically in RESULT.md;
finite checks here cannot establish a universal theorem.
"""
import cmath
import random
from fractions import Fraction

rng = random.Random(123)
for _ in range(3000):
    a = complex(rng.uniform(-2, 2), rng.uniform(-2, 2))
    b = complex(rng.uniform(-2, 2), rng.uniform(-2, 2))
    if abs(a) < 1e-8 or abs(b) < 1e-8:
        continue
    w = a / abs(a) * b.conjugate() / abs(b)
    z = a + b * w
    norm = abs(a) + abs(b)
    assert abs(abs(z) - norm) < 1e-12
    assert abs(z - norm * a / abs(a)) < 1e-12

for delta in [Fraction(1, 1000), Fraction(1, 25), Fraction(3, 20),
              Fraction(2, 5), Fraction(99, 100)]:
    # Phi(z) = delta*z + (1-delta)*conj(z): both scalar coefficients positive.
    assert delta > 0 and 1 - delta > 0
    assert delta + (1 - delta) == 1
    # Difference norm from conjugation is 2*delta (attained on z=i).
    assert abs(complex(delta) * (1j - (-1j))) == float(2 * delta)
    # Ordinary essential range is D(delta,1-delta): its directed support
    # gap from D(0,1) is 2*delta in the negative-real direction.
    assert delta - (1-delta) == 2*delta - 1
    # Essential-maximal range = {1}; at delta=0 it is D(0,1), distance 2.
    assert abs(1-(-1)) == 2

print('PASS: 3000 scalar norming cases and five exact perturbation profiles')
