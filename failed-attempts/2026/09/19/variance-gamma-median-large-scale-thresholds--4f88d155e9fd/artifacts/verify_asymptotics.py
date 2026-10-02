"""Numerical checks for the large-scale variance-gamma median asymptotics.

Requires Python 3 with SciPy. The parametrization is VG(r, theta, sigma, 0)
with density used in Fischer, Gaunt and Sarantsev (2025).
"""
import math
import scipy
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import betainc, gamma, kv

EULER_GAMMA = 0.5772156649015328606

def f_vg_positive(x, r, kappa):
    """VG(r,1,sqrt(kappa),0) density for x>0."""
    nu = (r - 1.0) / 2.0
    z = x * math.sqrt(1.0 + kappa) / kappa
    return (
        math.exp(x / kappa)
        / (math.sqrt(math.pi * kappa) * gamma(r / 2.0))
        * (x / (2.0 * math.sqrt(1.0 + kappa))) ** nu
        * kv(abs(nu), z)
    )

def cdf_zero(r, kappa):
    """Exact P[V <= 0] from the gamma-difference representation."""
    p = 0.5 - 0.5 / math.sqrt(1.0 + kappa)
    return betainc(r / 2.0, r / 2.0, p)

def cdf_positive(x, r, kappa):
    integral, _ = quad(
        lambda t: f_vg_positive(t, r, kappa),
        0.0,
        x,
        epsabs=2e-13,
        epsrel=2e-12,
        limit=300,
    )
    return cdf_zero(r, kappa) + integral

def numerical_median(r, kappa):
    target = lambda x: cdf_positive(x, r, kappa) - 0.5
    hi = max(1.0, r)
    while target(hi) < 0.0:
        hi *= 2.0
    return brentq(target, 0.0, hi, xtol=1e-13, rtol=1e-13, maxiter=100)

def asymptotic_median(r, kappa):
    sigma = math.sqrt(kappa)
    if r < 1.0:
        c = (
            r
            * 2.0**r
            * gamma((r + 1.0) / 2.0)
            / gamma((1.0 - r) / 2.0)
        ) ** (1.0 / r)
        return c * sigma ** (-(1.0 - r) / r)
    if r == 1.0:
        L = math.log(sigma)
        return 1.0 / (L + math.log(2.0 * L) + 1.0 - EULER_GAMMA)
    if r < 3.0:
        a = (
            2.0
            * ((r - 1.0) / 2.0) ** (r - 1.0)
            * gamma((3.0 - r) / 2.0)
            / (r * gamma((r - 1.0) / 2.0))
        )
        return (r - 1.0) + a * sigma ** (-(r - 1.0))
    if r == 3.0:
        return 2.0 + (4.0 / 3.0) * sigma**-2 * math.log(sigma)
    b = 2.0 * (r - 1.0) / (3.0 * (r - 3.0))
    return (r - 1.0) + b * sigma**-2

def normalized_ratio(r, kappa, numeric, asymptotic):
    if r <= 1.0:
        return numeric / asymptotic
    base = r - 1.0
    return (numeric - base) / (asymptotic - base)

cases = [
    (0.5, 1e6),
    (1.0, 1e6),
    (1.0, 1e10),
    (2.0, 1e6),
    (3.0, 1e6),
    (3.0, 1e10),
    (4.0, 1e6),
]

print("scipy_version=" + scipy.__version__)
print("r,kappa,numerical,asymptotic,normalized_ratio")
for r, kappa in cases:
    numeric = numerical_median(r, kappa)
    asymptotic = asymptotic_median(r, kappa)
    ratio = normalized_ratio(r, kappa, numeric, asymptotic)
    print(
        f"{r:g},{kappa:.0e},{numeric:.12g},"
        f"{asymptotic:.12g},{ratio:.12g}"
    )
