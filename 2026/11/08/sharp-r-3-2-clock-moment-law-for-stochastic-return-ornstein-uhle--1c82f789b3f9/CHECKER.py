"""Reproducible numerical checks for fast-clock OU return first-passage asymptotics.

Needs Python 3, SciPy and NumPy. These are finite-precision checks only;
the general theorem is analytical. All rates and units are dimensionless.
"""
import math
from scipy.integrate import quad
from scipy.special import erfc, erfcx, erfi

K2 = 2.0
v = math.sqrt(K2 / 2)
C = math.sqrt(math.pi / (2 * K2))
K = lambda x: C * erfcx(-v * x)
S = quad(lambda x: math.exp(K2 * x * x / 2), 0, 1, epsabs=1e-12)[0]
H = lambda x: erfi(v * x) / erfi(v)
M2 = quad(K, 0, 1, epsabs=1e-12)[0]

def integrate_kernel(q, f):
    return (quad(lambda x: q(x) * f(x), -math.inf, 0, epsabs=1e-12)[0]
            + quad(lambda x: q(x) * f(x), 0, 1, epsabs=1e-12)[0])

def mean_return(x):
    if x < 0:
        return quad(K, x, 0, epsabs=2e-11)[0]
    return H(x) * M2 - quad(K, 0, x, epsabs=2e-11)[0]

# Poisson clock W~Exp(1): exact killed-Brownian resolvent.
for rate in (25., 100., 400., 1600., 6400.):
    a = math.sqrt(rate)
    def q(x):
        return (math.exp(-a * abs(x)) - math.exp(-a * (2 - x))) / (2 * a)
    A = integrate_kernel(q, lambda x: x * K(x))
    p = math.exp(-a) + rate * quad(lambda x: q(x) * H(x), 0, 1, epsabs=1e-12)[0]
    if rate <= 1600:
        renewal_mean = ((integrate_kernel(q, lambda x: 1.)
                         + rate * integrate_kernel(q, mean_return)) / p)
        potential_mean = M2 - K2 * A / p
        assert abs(renewal_mean - potential_mean) < 1e-8
    if rate == 6400.:
        assert abs(A * rate ** 2 - 2) < 0.004
        assert abs(p * rate ** .5 - 1 / (2 * S)) < 0.0002
        assert abs((A / p) * rate ** 1.5 - 4 * S) < 0.01

# Deterministic and two-point reset clocks have the same mean as the
# Poisson clock, but different universal correction coefficients.
def heat_kernel(x, t):
    return ((math.exp(-x*x/(4*t)) - math.exp(-(2-x)**2/(4*t)))
            / math.sqrt(4 * math.pi * t))

def kernel_mean_F(t):
    if t == 0:
        return 0.
    return integrate_kernel(lambda x: heat_kernel(x,t), lambda x: x*K(x))

def test_clock(rate, atoms):
    A = 0.
    p = 0.
    for weight, w in atoms:
        t = w / rate
        A += weight * quad(kernel_mean_F, 0, t, epsabs=2e-11)[0]
        p += weight * (erfc(1/math.sqrt(4*t))
                       + quad(lambda x: heat_kernel(x,t)*H(x), 0, 1, epsabs=2e-11)[0])
    second = sum(weight*w*w for weight,w in atoms)
    root = sum(weight*math.sqrt(w) for weight,w in atoms)
    coefficient = S * math.sqrt(math.pi) * second / root
    assert abs(A*rate**2-second) < 0.02
    assert abs(p*rate**.5-root/(S*math.sqrt(math.pi))) < 0.002
    assert abs(A/p*rate**1.5-coefficient) < 0.04
    return coefficient

c_fixed = test_clock(1600., [(1.,1.)])
c_twopoint = test_clock(1600., [(.5,.5),(.5,1.5)])
assert c_fixed < c_twopoint < 4*S
print('PASS: Poisson renewal identity and asymptotic; deterministic and two-point clock asymptotics')
print('Theory: det=',c_fixed,'two-point=',c_twopoint,'Poisson=',4*S)
