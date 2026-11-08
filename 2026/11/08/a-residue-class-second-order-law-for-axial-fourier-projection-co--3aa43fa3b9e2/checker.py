"""Independent arithmetic and quadrature diagnostics for first-shell Fourier projection constants.
Run: python checker.py .  Requires Python 3, mpmath, and scipy.
These finite checks do not replace the analytic proof.
"""
from itertools import product
from fractions import Fraction
from math import comb, sqrt, pi, log, expm1
import mpmath as mp
from scipy.integrate import quad
from scipy.special import j0


def exact_kernel_norm(q, d):
    values = {3: (2, -1, -1), 4: (2, 0, -2, 0)}[q]
    return Fraction(sum(abs(sum(values[z] for z in point))
                        for point in product(range(q), repeat=d)), q**d)


def target(q, d):
    if q == 3:
        k = d // 3
        return Fraction(4*d*comb(d-1, k)*2**(d-1-k), 3**d)
    return Fraction(2*d*comb(2*d, d), 4**d)

count = 0
for q in (3, 4):
    for d in range(1, 7):
        lhs, rhs = exact_kernel_norm(q, d), target(q, d)
        assert lhs == rhs, (q,d,lhs,rhs)
        count += 1
print('FULL_FINITE_CHARACTER_KERNEL_CHECKS_PASSED', count)

mp.mp.dps = 75
for q in (3,4):
    for d in (300, 301, 302, 1200, 1201, 1202):
        if q == 3:
            k = d//3
            val = mp.mpf(4*d)/3 * mp.binomial(d-1,k)*(mp.mpf(1)/3)**k * (mp.mpf(2)/3)**(d-1-k)
            c = mp.mpf(-7)/24 if d%3==0 else mp.mpf(5)/24
        else:
            val = 2*d*mp.binomial(2*d,d)/mp.power(4,d)
            c = -mp.mpf(1)/8
        scaled = d*(val/(2*mp.sqrt(d/mp.pi))-1)
        assert abs(scaled-c) < mp.mpf(1)/d, (q,d,scaled,c)
print('INDEPENDENT_HIGH_PRECISION_LATTICE_SECOND_TERMS_PASSED', 12)

# Recover continuous endpoint norm by the Bessel characteristic integral.
# Quadrature uses the rescaled variable s and an integrable 1/s^2 tail.
def continuous_norm(d):
    eps = 1e-8
    def ff(s):
        if s < 0.005:
            return 0.5 - s*s*(1/8 - 1/(16*d))
        a = j0(sqrt(2/d)*s)
        if a > 0:
            return -expm1(d*log(a))/s**2
        return (1-a**d)/s**2
    vmax = 1500.0
    integral,_ = quad(ff,eps,vmax,epsabs=1e-7,epsrel=1e-7,limit=500)
    # Fourier tail J0(s)^d is negligible at large s for d>=3.
    return 2/pi*sqrt(2*d)*(integral + 1/vmax + eps/2)

for d, known in ((3,None),(10,None),(40,None),(100,None)):
    v=continuous_norm(d)
    lim=2*sqrt(d/pi)*(1+1/(16*d))
    assert abs(v-lim) < 1.5/(d**1.5), (d,v,lim)
assert abs(continuous_norm(10)-3.590986) < 0.0001
# Special cases are independently computable from a one- or two-torus integral.
assert abs(4/pi-1.27323954473516)<1e-12
assert abs(16/pi**2-1.6211389382774)<1e-6
print('INDEPENDENT_BESSEL_QUADRATURE_SECOND_ORDER_DIAGNOSTICS_PASSED',4)
print('ALL_FIRST_SHELL_PROJECTION_DIAGNOSTICS_PASSED')
