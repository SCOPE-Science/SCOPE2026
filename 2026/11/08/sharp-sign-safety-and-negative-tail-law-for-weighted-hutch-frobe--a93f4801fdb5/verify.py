"""Numerical and exact-rational checks for sign safety of weighted Hutch#.

Dependencies: Python 3.10+, numpy, scipy. This tests formulas and finite
instances; infinite statements are proved analytically in RESULT.md.
"""
from fractions import Fraction as F
from math import exp, gamma, lgamma, log, pi, sqrt
import numpy as np
from scipy.integrate import quad
from scipy.special import gammaincc, k1

checks = 0

# Exact-rational variance optimizer, and strict improvement over endpoints.
for r in range(1, 81):
    R = F(r)
    a = R / (R + 4)
    v = (1-a)**2/R + 4*a*a/(R*R)
    assert v == 4/(R*(R+4))
    assert v < F(1,r) and v < F(4,r*r)
    checks += 3

# Algebraic sign event equivalence and its unique constrained minimizer.
for n in range(1, 40):
    c = F(n + 4, n + 2)  # >=1, spanning a rational segment
    for ix in range(1, 31):
        x = F(ix, 5)
        for iy in range(1, 31):
            y = F(iy, 5)
            event = x*y > c*(x+y)
            equivalent = x > c and y > c and (x-c)*(y-c) > c*c
            assert event == equivalent
            checks += 1

# Gaussian rank-one matrix formula for every prescribed sketch width.
rng = np.random.default_rng(351289)
u = np.array([1., -2., 3.]); u = u / np.linalg.norm(u)
v = np.array([2., 1., -1., 4.]); v = v / np.linalg.norm(v)
sigma = 1.7
A = sigma*np.outer(u,v)
for r in [1, 2, 3, 4, 7, 16]:
    for alpha in [0., 0.2, 0.5, 1.]:
        omega = rng.standard_normal((4, r))
        psi = rng.standard_normal((3, r))
        s1 = np.linalg.norm(A@omega)**2/r
        s2 = np.linalg.norm(psi.T@A)**2/r
        s3 = np.linalg.norm(psi.T@A@omega)**2/r**2
        estimator = (1+alpha)*(s1+s2)/2-alpha*s3
        X = np.linalg.norm(v@omega)**2/r
        Y = np.linalg.norm(u@psi)**2/r
        scalar = sigma**2*((1+alpha)*(X+Y)/2-alpha*X*Y)
        assert np.isclose(estimator, scalar, rtol=2e-13, atol=2e-13)
        checks += 1


def probability(r, c):
    """Exact one-dimensional chi-square survival integral by quadrature."""
    k = r / 2
    def integrand(x):
        if x <= c: return 0.
        logf = k*log(k)-lgamma(k)+(k-1)*log(x)-k*x
        return exp(logf)*gammaincc(k, k*c*x/(x-c))
    return quad(integrand, c, max(40., 9.*c),
                epsabs=5e-25, epsrel=5e-9, limit=300)[0]


def asymptotic(r, c):
    rate = 2*c-1-log(2*c)
    return exp(-r*rate)/(sqrt(2*pi*r)*(2*c-1)*sqrt(4*c-1))

# r=2 has closed Bessel-K expression.
for c in [1., 1.25, 2., 4.]:
    q = probability(2, c)
    expected = 2*c*exp(-2*c)*k1(2*c)
    assert np.isclose(q, expected, rtol=5e-9, atol=2e-15)
    checks += 1

# Independent numerical integration approaches the sharp saddle prefactor.
for c in [1., 1.25]:
    ratios = []
    for r in [20, 40, 80]:
        q = probability(r, c)
        a = asymptotic(r, c)
        ratios.append(q/a)
        assert 0.7 < q/a < 1.04
        checks += 1
    assert ratios[0] < ratios[1] < ratios[2]
    checks += 1

# Optimal-weight sign-probability relative to unweighted asymptotic e^-2.
ratios = []
for r in [20, 40, 80]:
    q1 = probability(r, 1.)
    qopt = probability(r, 1.+2./r)
    ratios.append(qopt/q1)
    assert 0.05 < qopt/q1 < 0.16
    checks += 1
assert ratios[0] < ratios[1] < ratios[2] < exp(-2.)
checks += 1

# Exact open-set negative witness for any alpha>0, any rank-one nonzero A.
for r in [1, 2, 5, 10]:
    for n in range(1, 20):
        alpha = F(n, 20)
        t2 = F(r)*(1+alpha)/alpha+1
        value = (1+alpha)*t2/F(r)-alpha*t2*t2/F(r*r)
        assert value < 0
        checks += 1

print('VERIFY_OK', checks, 'checks')
