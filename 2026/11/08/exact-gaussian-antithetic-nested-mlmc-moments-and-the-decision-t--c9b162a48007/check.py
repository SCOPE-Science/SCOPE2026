"""Reproduce the Gaussian antithetic nested-MLMC second-moment formula.

Run with Python 3.9+ using the standard library: python check.py
The exact mathematical proof is in RESULT.md; numerical quadrature is diagnostic.
"""
import math
import random

PI = math.pi


def exact_moment(n, tau, sigma=1.0):
    assert n >= 1 and int(n) == n and tau >= 0 and sigma > 0
    k = n * (tau / sigma) ** 2
    a = math.sqrt(2 * k + 1)
    return sigma ** 2 / (2 * PI * n) * ((k + 1) * math.atan(1 / a) - a / 2)


def direct_angle_moment(n, tau, sigma=1.0, steps=4000):
    """Separate numerical evaluation of the positive-quadrant Gaussian polar integral."""
    a = math.sqrt(0.5 + n * (tau / sigma) ** 2)
    b = math.sqrt(0.5)
    endpoint = math.atan(b / a)
    h = endpoint / steps

    def integrand(theta):
        return (b * math.cos(theta) - a * math.sin(theta)) ** 2

    weighted = integrand(0) + integrand(endpoint)
    for i in range(1, steps):
        weighted += (4 if i % 2 else 2) * integrand(i * h)
    integral = weighted * h / 3
    return sigma ** 2 / (4 * n) * 4 / PI * integral


def empirical_moment(n, tau, sigma=1.0, samples=250000, seed=1729):
    rng = random.Random(seed)
    total = 0.0
    for _ in range(samples):
        y = rng.gauss(0, tau)
        z0, z1 = rng.gauss(0, 1), rng.gauss(0, 1)
        x0 = y + sigma * z0 / math.sqrt(n)
        x1 = y + sigma * z1 / math.sqrt(n)
        delta = max(0, (x0+x1)/2) - (max(0,x0)+max(0,x1))/2
        total += delta**2
    return total / samples


def main():
    checks = 0
    for n in (1, 2, 5, 17, 80):
        for tau in (0, 0.05, 0.3, 1.0, 2.0):
            for sigma in (0.3, 1.0, 2.0):
                exact = exact_moment(n, tau, sigma)
                numerical = direct_angle_moment(n, tau, sigma)
                assert exact > 0
                assert math.isclose(exact, numerical, rel_tol=1e-9, abs_tol=1e-13), (n,tau,sigma,exact,numerical)
                checks += 1
    for n in (1, 2, 5, 17, 80):
        atom = exact_moment(n, 0, 1)
        assert math.isclose(n*atom,(PI-2)/(8*PI),rel_tol=1e-12)
        checks += 1
    for n,tau in ((3,0), (3,1), (11,0.15), (11,1.0)):
        exact = exact_moment(n,tau)
        empirical = empirical_moment(n,tau)
        assert abs(empirical/exact - 1) < 0.04, (n,tau,exact,empirical)
        checks += 1
    tau = 1.3
    limit = 1/(6*PI*math.sqrt(2)*tau)
    for n in (1000,5000):
        ratio = (n**1.5)*exact_moment(n,tau)/limit
        assert abs(ratio-1) < 0.003,(n,ratio)
        checks += 1
    print('PASS',checks,'numeric checks including independent polar quadrature and seeded Monte Carlo')
    print('atomic coefficient', (PI-2)/(8*PI))
    print('smooth Gaussian coefficient tau=1', 1/(6*PI*math.sqrt(2)))

if __name__ == '__main__':
    main()
