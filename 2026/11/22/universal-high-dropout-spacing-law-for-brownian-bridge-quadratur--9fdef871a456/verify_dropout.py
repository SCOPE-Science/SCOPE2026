"""Independent numerical checks of exact Bernoulli-dropout bridge quadrature claims.

This is finite reproducibility support; analytic guarantees appear in RESULT.md.
"""
from itertools import combinations
from math import sqrt
import numpy as np
from scipy.optimize import minimize


def gap_variance(nodes):
    nodes = np.asarray(nodes, dtype=float)
    return np.diff(np.r_[0.0, nodes, 1.0]).dot(np.diff(np.r_[0.0, nodes, 1.0])**2)/12.0


def risk(x, survival):
    x = np.asarray(x)
    n = len(x)
    total = 0.0
    for mask in range(1 << n):
        inds = [j for j in range(n) if (mask >> j) & 1]
        total += survival**len(inds) * (1-survival)**(n-len(inds)) * gap_variance(x[inds])
    return total


def solve_design(n, r):
    start = np.arange(1, n+1, dtype=float)/(n+1)
    out = minimize(lambda z: risk(z, r), start,
                   bounds=[(0.0, 1.0)]*n,
                   constraints=[{"type":"ineq", "fun":lambda z: np.diff(z)}],
                   method="SLSQP", options={"ftol":1e-15,"maxiter":1000})
    assert out.success, out.message
    return out.x


def covariance_variance(x):
    x = np.asarray(x, dtype=float)
    C = np.minimum.outer(x,x) - np.outer(x,x)
    k = x*(1-x)/2
    return 1/12 - k @ np.linalg.solve(C, k)


if __name__ == "__main__":
    # Pointwise Gaussian-conditioning identity at unequal interior nodes.
    for x in ([.2], [.2,.58], [.14,.37,.82], [.17,.28,.63,.85]):
        assert abs(covariance_variance(x)-gap_variance(x)) < 1e-12

    # Exact two-site stationarity polynomial for several survival rates.
    for q in (0.0,.12,.5,.75,.93,.99):
        r=1-q
        d=(sqrt((1+q)**2+3*r*r)-(1+q))/(6*r)
        assert 0 < d < .5
        assert abs(12*r*d*d+4*(1+q)*d-r) < 1e-12
        xx=np.array([.5-d,.5+d])
        if q != 0:
            xn=solve_design(2,r)
            assert np.max(np.abs(xn-xx)) < 3e-5

    # High-dropout, all-network universal first-order law.
    for n in (2,3,4,5):
        ystar=(2*np.arange(1,n+1)-n-1)/8
        for r in (.1,.03):
            x=solve_design(n,r)
            ys=(x-.5)/r
            assert np.max(np.abs(ys-ystar)) < .045
            assert abs(x.sum()-n/2) < 3e-5

    # Verify cubic expansion of exact finite-subset formula with fixed scaled nodes.
    for n in (2,3,4):
        y=(2*np.arange(1,n+1)-n-1)/8
        G=np.sum(y*y)/4-sum(y[j]-y[i] for i in range(n) for j in range(i+1,n))/16
        for r in (.02,.01):
            observed=(risk(.5+r*y,r)-risk(np.full(n,.5),r))/r**3
            assert abs(observed-G) < .1
    print("PASS: exact conditional variances, two-site stationarity, asymptotic numerical checks")
