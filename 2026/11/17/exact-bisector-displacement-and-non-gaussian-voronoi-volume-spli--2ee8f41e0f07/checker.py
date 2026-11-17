"""Reproducibility checks for two-site Voronoi splitting in Euclidean balls.

Only standard numerical checks are made; the analytic proof is in RESULT.md.
Run: python checker.py
"""
import math
from fractions import Fraction
import numpy as np
from scipy import integrate, special, stats


def ball_volume(d):
    return math.exp((d / 2) * math.log(math.pi) - special.gammaln(1 + d / 2))


def density_h(d, h):
    h = abs(float(h))
    if h >= 1:
        return 0.0
    c = 2**d * d * (ball_volume(d - 1) / ball_volume(d))
    integrand = lambda r: r**(d - 1) * max(0, 1 - (r + h)**2)**((d - 1)/2)
    return c * integrate.quad(integrand, 0, 1 - h, epsabs=2e-12)[0]


def density_zero(d):
    return math.exp((d-2)*math.log(2) + 2*math.log(d)
                    + 2*special.gammaln(d/2) - 0.5*math.log(math.pi)
                    - special.gammaln(d + 0.5))


def sample(d, n, seed):
    rng = np.random.default_rng(seed)
    a = rng.normal(size=(n, d))
    b = rng.normal(size=(n, d))
    a /= np.linalg.norm(a, axis=1)[:, None]
    b /= np.linalg.norm(b, axis=1)[:, None]
    ra = rng.random(n)**(1/d)
    rb = rng.random(n)**(1/d)
    # Stable formula for the bisector offset as d increases.
    cos = np.einsum('ij,ij->i', a, b)
    h = (ra**2 - rb**2)/(2*np.sqrt(ra**2 + rb**2 - 2*ra*rb*cos))
    c = math.exp(special.gammaln(d/2+1) - special.gammaln((d+1)/2) - 0.5*math.log(math.pi))
    # Exact sectional cap-volume primitive via symmetric incomplete beta.
    im = -np.sign(h)*special.betainc(0.5, (d+1)/2, h*h)
    return h, im


def exact_three_dimensional_moment():
    # Integrate the polynomial 2*(3/5)*(4+h)*(1-h)^4*((3h-h^3)/2)^2.
    coeff = [Fraction(0) for _ in range(6)]
    for k in range(5):
        q = Fraction((-1)**k * math.comb(4, k))
        coeff[k] += 4*q
        coeff[k+1] += q
    return Fraction(3, 10)*sum(
        (c*(Fraction(9,k+3)-Fraction(6,k+5)+Fraction(1,k+7))
         for k,c in enumerate(coeff)),Fraction(0))


def main():
    assert exact_three_dimensional_moment() == Fraction(421, 4200)
    for d in (2, 3, 4, 5, 6):
        norm = 2*integrate.quad(lambda h: density_h(d,h), 0, 1, epsabs=2e-9)[0]
        assert abs(norm-1) < 1e-8, (d,norm)
        assert abs(density_h(d, 0)-density_zero(d)) < 1e-8
    for h in (0.0, 0.1, 0.25, 0.5, 0.75, 0.9):
        assert abs(density_h(3,h) - 0.6*(4+h)*(1-h)**4)<1e-10
    h,im=sample(3, 140000, 20261113)
    assert abs(np.mean(h*h) - 1/20) < .0017
    assert abs(np.mean(im*im) - 421/4200)<.002
    assert abs(np.mean(abs(im)) - 26/105)<.003
    for d in (64,128,256):
        h,im=sample(d, 60000, 20261113+d)
        ks_h=stats.kstest(d*h,'laplace',args=(0,1/math.sqrt(2))).statistic
        ks_im=stats.kstest(math.sqrt(d)*im,'laplace',args=(0,1/math.sqrt(math.pi))).statistic
        assert ks_h < .035 and ks_im < .045,(d,ks_h,ks_im)
    print('TWO_SITE_VORONOI_CHECKS_OK')

if __name__ == '__main__':
    main()
