"""Independent finite numerical checks for two-node Gaussian kernel quadrature.

Run: python verify.py (requires numpy and scipy). The infinite-dimensional
or infinite-parameter claims are established analytically, not by this script.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import betainc, gammaln

rng = np.random.default_rng(20261118)
checks = 0


def check(test, description):
    global checks
    checks += 1
    if not bool(test):
        raise AssertionError(f"check {checks}: {description}")


def predicted_positive(d, h):
    a = 1.0 + 2.0 * h
    return betainc(0.5, d / 2, a * a / (1.0 + a * a))


def pair_weights(x, y, h):
    d = x.size
    a = (1.0 + 2.0 * h) ** (-d / 2)
    q = a * np.exp(-h * np.array([x @ x, y @ y]) / (1.0 + 2.0 * h))
    k = math.exp(-h * ((x - y) @ (x - y)))
    return np.linalg.solve(np.array([[1.0, k], [k, 1.0]]), q)


# Kernel means via independent one-dimensional integration.
for h in (0.1, 0.5, 2.0):
    for z in (-1.8, -0.7, 0.0, 0.9, 1.4):
        direct = quad(lambda u: math.exp(-h * (z-u)**2-u*u/2)/math.sqrt(2*math.pi),
                      -12, 12, epsabs=2e-12)[0]
        predicted = (1+2*h)**(-0.5)*math.exp(-h*z*z/(1+2*h))
        check(abs(direct-predicted)<2e-11, "integrated kernel mean")

# Check exact sign inequality against two-by-two linear solve.
for d in (1,2,3,6,12):
    for h in (0.015,0.08,0.4,1.0,3.0):
        a = rng.normal(size=(120,d))
        b = rng.normal(size=(120,d))
        for x,y in zip(a,b):
            ratio = abs(x@x-y@y)/((x-y)@(x-y))
            pred = ratio < 1+2*h
            weights = pair_weights(x,y,h)
            check(np.all(np.isfinite(weights)), "finite exact weights")
            if abs(ratio-(1+2*h))>1e-8:
                check(bool(np.all(weights>0)) == bool(pred), "sharp positivity condition")

# Monte Carlo (large independent sample) against exact regularized incomplete beta.
for d in (1,2,3,4,6,10):
    n = 60000
    A = rng.normal(size=(n,d))
    B = rng.normal(size=(n,d))
    dist = np.sum((A-B)**2, axis=1)
    ratio = np.abs(np.sum(A*A,axis=1)-np.sum(B*B,axis=1))/dist
    for h in (0.04,0.3,1.3):
        estimate = np.mean(ratio < 1+2*h)
        exact = predicted_positive(d,h)
        check(abs(estimate-exact)<0.012, "sample frequency and beta probability")

# Student-t special cases: d=1 and d=2; monotonic dimensions and bandwidths.
for h in (0.01,0.3,1.0,10.0):
    a = 1+2*h
    check(abs(predicted_positive(1,h)-2*math.atan(a)/math.pi)<1e-13, "dimension one")
    check(abs(predicted_positive(2,h)-a/math.sqrt(1+a*a))<1e-13, "dimension two")
    for d in range(1,13):
        check(predicted_positive(d+1,h) >= predicted_positive(d,h), "dimension monotonicity")
        check(predicted_positive(d,h+0.1) >= predicted_positive(d,h), "bandwidth monotonicity")
check(predicted_positive(5,1e-12) < .95 < predicted_positive(6,1e-12), "six-dimensional reliability threshold")

# Exact t^{-d} tail prefactor and large-d exponential asymptotic.
for d in range(1,9):
    coefficient = math.exp(gammaln((d+1)/2)-d*math.log(2)-.5*math.log(math.pi)-gammaln(d/2+1))
    for t in (100,1000):
        survival = 1-predicted_positive(d,t)
        # Direct lower-tail beta avoids cancellation in high dimension.
        z = 1/(1+(1+2*t)**2)
        survival = betainc(d/2, .5, z)
        check(abs(survival*t**d/coefficient-1)<0.06, "polynomial critical-horizon tail")

for a in (1.0, 1.4, 3.0):
    h = (a-1)/2
    for d in (100,200,400):
        z = 1/(1+a*a)
        exact = betainc(d/2, .5, z)
        approx = math.sqrt(2*(1+a*a)/(math.pi*d*a*a))*((1+a*a)**(-d/2))
        if exact > 0 and approx > 0:
            check(abs(exact/approx-1) < 0.065, "fixed-h large-d law")

print(f"PASS: {checks} finite tests; all derived two-node identities reproduced")
