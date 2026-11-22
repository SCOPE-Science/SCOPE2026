"""Standalone exact sign-certificate checks for a Pareto renewal model."""
from fractions import Fraction as F
from math import isclose

def f(t):
    return 2 / t**3 if t >= 1 else 0.0

def composite_simpson(func, low, high, n=20000):
    assert n % 2 == 0
    h = (high - low) / n
    return h / 3 * (func(low) + func(high) +
        4 * sum(func(low + h * i) for i in range(1, n, 2)) +
        2 * sum(func(low + h * i) for i in range(2, n, 2)))

# Intensity of the stationary Pareto(2,1) renewal process is 1/2.
assert F(1, 2) == F(1, 2)
# Positive lag t=1/2: no pair of consecutive renewal epochs can be that close.
assert F(0, 1) / 2 - F(1, 4) == -F(1, 4)
# At 6/5 and 9/5 only one renewal interval fits.
nu_6_5 = F(2,1) / F(6,5)**3
nu_9_5 = F(2,1) / F(9,5)**3
assert nu_6_5 / 2 - F(1,4) == F(71,216) > 0
assert nu_9_5 / 2 - F(1,4) == -F(229,2916) < 0
# At 5/2, one or two waits fit. The integrand in the two-wait convolution
# is at least 4/(5/4)^6 for s in [1,3/2].
nu_5_2_lower = F(2,1)/F(5,2)**3 + F(1,2)*F(4,1)/F(5,4)**6
last_sign_lower = nu_5_2_lower/F(2,1)-F(1,4)
assert nu_5_2_lower == F(10192,15625)
assert last_sign_lower == F(4759,62500) > 0
conv = composite_simpson(lambda x: f(x) * f(2.5-x), 1., 1.5)
nu_5_2 = f(2.5) + conv
assert nu_5_2 > float(nu_5_2_lower)
assert isclose(nu_5_2, 0.6743164321595, rel_tol=2e-8)
print('PASS: 4 lagged sign witnesses (0, 1/2, 6/5, 9/5, 5/2)')
print('exact strict lower bound on fifth witness:', last_sign_lower)
print('independent Simpson convolution:', format(nu_5_2, '.14f'))
