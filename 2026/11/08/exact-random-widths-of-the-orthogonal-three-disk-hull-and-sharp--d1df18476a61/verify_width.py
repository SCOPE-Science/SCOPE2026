"""Reproducible numerical checks for random widths of coordinate-hyperdisk hulls.

Dependencies: Python 3, NumPy, SciPy. Numerical experiments corroborate,
but do not substitute for, the analytic statements in RESULT.md.
"""
import math
import numpy as np
from scipy.integrate import quad

SEED = 20261101
rng = np.random.default_rng(SEED)


def cdf_three(w):
    lower = 2 * math.sqrt(2 / 3)
    if w <= lower:
        return 0.0
    if w >= 2:
        return 1.0
    t = math.sqrt(1 - w*w/4)
    return (-2 - 3*t + 12 / math.pi *
            (t*math.asin(t / math.sqrt(1-t*t)) +
             math.atan(math.sqrt(1-2*t*t))))


def independent_integral(t):
    if t <= 0:
        return 1.0
    if t >= 1 / math.sqrt(3):
        return 0.0
    q = quad(lambda s: 1-4/math.pi*math.asin(s/math.sqrt(1-s*s)),
             0, t, epsabs=1e-12)[0]
    return 1-3*q


def lower_coefficient(d):
    return (d ** (d-0.5) * (d-1) ** ((d-1)/2) *
            math.gamma(d/2)/(math.pi**(d/2)*math.factorial(d-1)))


def upper_coefficient(d):
    return (2*d*math.gamma(d/2) /
            (math.sqrt(math.pi)*math.gamma((d-1)/2)))


def finite_disk_support(u, j, sample=16384):
    # Approximate an orthogonal-disk support maximization directly,
    # without computing min(abs(u)) or using the theorem's support identity.
    others = [i for i in range(3) if i != j]
    theta = 2*math.pi*np.arange(sample)/sample
    return np.max(u[others[0]]*np.cos(theta)+u[others[1]]*np.sin(theta))


def check():
    lower = 2*math.sqrt(2/3)
    assert cdf_three(lower) == 0 and cdf_three(2) == 1
    assert abs(independent_integral(1/math.sqrt(3))-0) < 1e-14

    # Equality with an independent one-dimensional spherical band integral.
    for w in np.linspace(lower+1e-5,2-1e-5,81):
        t = math.sqrt(1-w*w/4)
        assert abs(cdf_three(w)-independent_integral(t)) < 8e-13
    assert all(cdf_three(a) <= cdf_three(b)+1e-12
               for a,b in zip(np.linspace(lower,2,200)[:-1],
                              np.linspace(lower,2,200)[1:]))

    # Sharp lower and upper endpoint coefficients.
    assert abs(cdf_three(lower+1e-4)/(1e-4**2) /
               lower_coefficient(3)-1) < 2e-4
    assert abs((1-cdf_three(2-1e-6))/(1e-6**0.5) /
               upper_coefficient(3)-1) < 8e-4

    # Directly maximize over sampled point sets from each generating disk.
    for u in rng.normal(size=(30,3)):
        u /= np.linalg.norm(u)
        numerical = 2*max(finite_disk_support(u,j) for j in range(3))
        formula = 2*math.sqrt(1-np.min(u*u))
        assert 0 <= formula-numerical < 1e-7

    # Independent Haar-sphere Monte Carlo, with a deterministic seed.
    sample_size = 400000
    z = rng.normal(size=(sample_size,3))
    z /= np.linalg.norm(z,axis=1)[:,None]
    widths = 2*np.sqrt(1-np.min(z*z,axis=1))
    for w in [1.64,1.65,1.7,1.75,1.8,1.9,1.95,1.99]:
        p = cdf_three(w)
        empirical = np.count_nonzero(widths <= w)/sample_size
        sigma = math.sqrt(p*(1-p)/sample_size)
        assert abs(empirical-p) < 6*sigma+0.0015

    # Gaussian-coordinate extreme-value scaling (quantile check, not proof).
    target = math.pi/2*math.log(2)**2
    observed = []
    for d in [30,100,300]:
        values = []
        for _ in range(40):
            zz = rng.normal(size=(1000,d))
            min_sq = np.min(zz*zz,axis=1)
            total = np.sum(zz*zz,axis=1)
            values.append(d**3*(2-2*np.sqrt(1-min_sq/total)))
        observed.append(float(np.median(np.concatenate(values))))
    assert abs(observed[-1]-target) < 0.14
    print('THREE_DIMENSIONAL_CDF_AND_ENDPOINT_CHECKS_PASSED')
    print('DIRECT_DISK_SUPPORT_AND_MONTE_CARLO_CHECKS_PASSED')
    print('GAUSSIAN_HIGH_DIMENSIONAL_SCALING_CHECKS_PASSED')


if __name__ == '__main__':
    check()
