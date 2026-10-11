from fractions import Fraction


def tau(mu, a, b, c):
    return c * (mu ** a) / ((mu ** a) + b)


def denominator(mu, x2, zeta, a, b, c):
    t = tau(mu, a, b, c)
    return mu * x2 + t * zeta


def delta_star(mu, x2, zeta, a, b, c):
    t = tau(mu, a, b, c)
    d = denominator(mu, x2, zeta, a, b, c)
    assert d > 0
    return t * mu / d


def derivative_at_zero(mu, tau_value, x2, zeta, delta):
    return zeta + mu * x2 / tau_value - mu / delta


# Check the minimizer-sign threshold around delta_star.
mu = 1e-4
x2 = 2.0
zeta = -0.3
a, b, c = 2.0, 1.0, 1.0
t = tau(mu, a, b, c)
ds = delta_star(mu, x2, zeta, a, b, c)
assert derivative_at_zero(mu, t, x2, zeta, 0.5 * ds) < 0
assert abs(derivative_at_zero(mu, t, x2, zeta, ds)) < 1e-11
assert derivative_at_zero(mu, t, x2, zeta, 2.0 * ds) > 0

# a>1: positivity and delta_star/tau -> 1/x2.
ratios = []
for k in (4, 6, 8, 10):
    m = 10.0 ** (-k)
    assert denominator(m, 2.0, -1.0, 2.0, 1e-3, 1.0) > 0
    ratios.append(delta_star(m, 2.0, -1.0, 2.0, 1e-3, 1.0) / tau(m, 2.0, 1e-3, 1.0))
assert abs(ratios[-1] - 0.5) < abs(ratios[0] - 0.5)
assert abs(ratios[-1] - 0.5) < 1e-6

# a<1: eventual negativity.
for k in (8, 10, 12):
    m = 10.0 ** (-k)
    assert denominator(m, 2.0, -1.0, 0.5, 1e-3, 1.0) < 0

# a=1: both strict coefficient-sign cases.
for m in (1e-6, 1e-9, 1e-12):
    assert denominator(m, 2.0, -0.1, 1.0, 1.0, 1.0) > 0
    assert denominator(m, 2.0, -3.0, 1.0, 1.0, 1.0) < 0

# Exact critical line with rational arithmetic:
# x2=2, b=3, c=6, zeta=-1 gives x2+(c/b)zeta=0.
x2q, bq, cq, zq = map(Fraction, (2, 3, 6, -1))
for den in (10, 1000, 10**8):
    m = Fraction(1, den)
    tq = cq * m / (m + bq)
    dq = m * x2q + tq * zq
    assert dq == x2q * m * m / (m + bq)
    assert dq > 0
    dsq = tq * m / dq
    assert dsq == cq / x2q == 3

print('VERIFY_OK')
