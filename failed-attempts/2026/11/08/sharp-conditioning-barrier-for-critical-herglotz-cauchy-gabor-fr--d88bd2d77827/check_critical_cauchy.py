"""Reproducibility checks for sharp frame conditioning of positive Cauchy sums.

Requires Python 3 standard library only. Numerical checks corroborate, but do not prove,
the universal Zak-transform and scalar-optimization arguments in RESULT.md.
"""
import cmath
import math
import random

rng = random.Random(271828)
TAU = 2.0 * math.pi
STAR = math.sqrt(2.0) - 1.0
C = (1.0 + math.sqrt(2.0)) ** 2
checks = 0


def zfiber(poles, alpha, x, s):
    # Its modulus equals the alpha-Zak transform modulus, multiplied by alpha/(2pi).
    z = cmath.exp(-1j * TAU * x)
    return sum(a * math.exp(-(1.0 - s) * TAU * w / alpha) /
               (1.0 - math.exp(-TAU * w / alpha) * z) for a, w in poles)


def exact_bounds(poles, alpha):
    upper = sum(a / (1.0 - math.exp(-TAU * w / alpha)) for a, w in poles)
    lower = sum(a / (math.exp(TAU * w / alpha) + 1.0) for a, w in poles)
    return (TAU * lower)**2 / alpha, (TAU * upper)**2 / alpha


for n in range(1, 7):
    for _ in range(30):
        alpha = math.exp(rng.uniform(-1.2, 1.2))
        poles = [(math.exp(rng.uniform(-2, 2)), alpha * math.exp(rng.uniform(-3.0, 1.5)))
                 for j in range(n)]
        A, B = exact_bounds(poles, alpha)
        assert A > 0 and B >= A
        checks += 1
        for j in range(28):
            x, s = rng.random(), rng.random()
            test = (TAU**2 / alpha) * abs(zfiber(poles, alpha, x, s)) ** 2
            assert A * (1 - 1e-12) <= test <= B * (1 + 1e-12), (A, test, B)
            checks += 1
        # Endpoint limits must be the exact formulas, to 1e-6 relative accuracy.
        eps = 1e-9
        low = (TAU**2 / alpha) * abs(zfiber(poles, alpha, 0.5, eps)) ** 2
        up = (TAU**2 / alpha) * abs(zfiber(poles, alpha, 0., 1.-eps)) ** 2
        assert abs(low/A-1.) < 1e-6 and abs(up/B-1.) < 1e-6
        checks += 2
        rvals = [math.exp(-TAU * w / alpha) for a, w in poles]
        v = [a * r/(1+r) for (a,w),r in zip(poles,rvals)]
        delta = sum(vj*(r-STAR)**2/(r*(1-r)) for vj,r in zip(v,rvals))/sum(v)
        assert math.isclose(B/A, C**2 * (1+delta)**2, rel_tol=4e-13)
        assert B/A >= C**2*(1-1e-13)
        checks += 2

# The sharp optimum for a single pole is unique within this family.
for step in range(-50, 51):
    r = 1/(1+math.exp(-0.1*step))
    h = (1+r)/(r*(1-r))
    assert math.isclose(h-C, C*(r-STAR)**2/(r*(1-r)), rel_tol=5e-12, abs_tol=1e-12)
    checks += 1
wstar = math.log(1+math.sqrt(2))/TAU
A, B = exact_bounds([(1., wstar)], 1.)
assert math.isclose(B/A,(1+math.sqrt(2))**4,rel_tol=1e-13)
checks += 1

# Independent finite symmetric Zak series, using the raw rational Cauchy window.
# The full Zak sum converges conditionally; truncations are only numerical checks.
for _ in range(20):
    poles = [(0.5+rng.random(), 0.04+0.3*rng.random()) for j in range(2)]
    x = 0.1+0.8*rng.random()
    s = 0.15+0.7*rng.random()
    raw = 0j
    for k in range(-24000, 24001):
        raw += sum(a/(x+k-1j*w) for a,w in poles)*cmath.exp(-1j*TAU*k*s)
    expected = TAU*1j*cmath.exp(-1j*TAU*(1-s)*x)*zfiber(poles,1.,x,s)
    assert abs(raw-expected) < .0015, (raw, expected)
    checks += 1

print('CRITICAL_CAUCHY_FRAME_CHECKS_PASS', checks)
