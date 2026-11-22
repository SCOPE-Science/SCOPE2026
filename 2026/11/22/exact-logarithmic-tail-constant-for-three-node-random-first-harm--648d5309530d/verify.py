"""Finite diagnostic checks for random first-harmonic circle quadrature.

Analytic limit and moment claims are established by the companion proof,
not by numerical tests.
"""
import math
import numpy as np


def weights(a, b):
    c = 2 * math.pi - a - b
    den = math.sin(a) + math.sin(b) + math.sin(c)
    return np.array([math.sin(b), math.sin(c), math.sin(a)]) / den


def homogeneous(a, b):
    r = a + b
    x = a / r
    return 2 * math.sqrt(2 * (x*x - x + 1)) / (r*r*x*(1-x))


def H(x):
    return math.sqrt(2 * (x*x - x + 1)) / (x*(1-x))


def main():
    rng = np.random.default_rng(20260908)
    assertions = 0
    for _ in range(1500):
        g = rng.dirichlet([1., 1., 1.]) * (2*math.pi)
        a, b, c = map(float, g)
        w = weights(a, b)
        m = np.array([[1., 1., 1.],
                      [1., math.cos(a), math.cos(a+b)],
                      [0., math.sin(a), math.sin(a+b)]])
        wsolve = np.linalg.solve(m, np.array([1., 0., 0.]))
        assert np.max(np.abs(w-wsolve)) < 1.e-6
        assertions += 1
        assert np.max(np.abs(m@w-np.array([1., 0., 0.]))) < 1.e-6
        assertions += 1
    for r in [0.1, 0.03, 0.01, 0.003]:
        for x in [0.01, 0.1, 0.45, 0.9, 0.99]:
            a, b = r*x, r*(1-x)
            ratio = np.linalg.norm(weights(a,b))/homogeneous(a,b)
            assert abs(ratio-1) <= 0.6 * r*r
            assertions += 1
    # The Jacobian-transformed homogeneous corner integral: sample on a
    # logit grid, whose endpoint resolution follows the logarithmic scale.
    for log_t in [16., 24., 32.]:
        T=math.exp(log_t)
        cutoff=T*(0.1**2)/2
        y=np.linspace(-log_t-4, log_t+4, 200001)
        x=1/(1+np.exp(-y))
        x=np.clip(x, 1.e-15, 1-1.e-15)
        hv=np.sqrt(2*(x*x-x+1))/(x*(1-x))
        I=np.trapezoid(np.minimum(cutoff, hv)*x*(1-x), y)
        assert abs(I/log_t-2*math.sqrt(2)) < 1.1
        assertions += 1
    assert abs(3*math.sqrt(2)/math.pi**2 - .42986937618806725)<1.e-13
    assertions += 1
    print(f'CHECK_OK assertions={assertions}; finite diagnostics only')

if __name__=='__main__':
    main()
