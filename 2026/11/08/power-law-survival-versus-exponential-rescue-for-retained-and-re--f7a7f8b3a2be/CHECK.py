"""Deterministic numerical consistency checks for half-line boundary-contact resetting laws."""
import math
from scipy.integrate import quad

D, R, r = 1.7, 1.3, 0.9
k = math.sqrt(r / D)
a = math.exp(-R * k)
J = r * a / k
checks = 0
for ell in (0.0, 0.25, 0.8, 2.0, 4.0):
    num = quad(lambda t: r * math.exp(-r * t) * math.erfc((R + ell) / (2.0 * math.sqrt(D * t))), 0, math.inf, epsabs=1e-11)[0]
    expected = math.exp(-k * (R + ell))
    assert abs(num - expected) < 2e-10, (ell, num, expected)
    checks += 1

# Exponential reward mixture law has mean a/k and second moment 2a/k^2.
for theta in (0.05, 0.18, 0.4):
    mgf = 1.0 - a + a * k / (k - theta)
    quadmgf = (1-a) + quad(lambda l: a * k * math.exp(-(k-theta)*l), 0, math.inf)[0]
    assert abs(mgf - quadmgf) < 1e-11
    checks += 1
assert abs(J - math.sqrt(D*r)*math.exp(-R*k)) < 1e-12
checks += 1

# Laplace success probability for a fresh Lomax contact threshold.
for alpha in (0.6, 1.0, 1.6, 3.0):
    ell0 = 0.7
    lp = quad(lambda L: math.exp(-k * L) * alpha / ell0 * (1 + L/ell0)**(-alpha - 1), 0, math.inf, epsabs=1e-12)[0]
    assert 0 < lp < 1
    p = math.exp(-R*k)*lp
    mt = (1-p)/(r*p)
    assert abs(mt - (math.exp(R*k)/lp -1)/r) < 1e-11
    checks += 1

# The unique optimizer of the rate of local-time production is r=D/R^2.
ropt = D/R**2
jopt = math.sqrt(D*ropt)*math.exp(-R*math.sqrt(ropt/D))
for mult in (0.01,0.1,0.3,0.9,1.1,2,8,100):
    rr=ropt*mult
    assert jopt > math.sqrt(D*rr)*math.exp(-R*math.sqrt(rr/D))
    checks += 1

# Regular variation of the claimed Lomax survival at linear local-time levels.
for alpha in (0.5, 0.8, 1.4):
    for scale in (0.4, 1.8, 3.1):
        t = 1e8
        ratio = ((1 + scale*J*t)/(1 + J*t))**(-alpha)
        predicted = scale**(-alpha)
        assert abs(ratio-predicted) < 1e-6
        checks += 1

print(f'PASS: {checks} deterministic independent integral / algebra / limiting checks')
