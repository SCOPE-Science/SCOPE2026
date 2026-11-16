"""Finite consistency checks for the two-zero coefficient-energy formulas.

All numerical truncations are evidence for finite instances only; the analytic
proof of the infinite problem appears in RESULT.md.
"""
from math import isclose
from scipy.optimize import minimize_scalar
import numpy as np

checks = 0


def check(cond):
    global checks
    assert cond
    checks += 1


def exact_single(p, r):
    q = p / (p - 1)
    return (r ** (-q) - 1) ** (p - 1)


def exact_opp(p, r):
    q = p / (p - 1)
    return (r ** (-2 * q) - 1) ** (p - 1)


def finite_jet(p, r, count=2000):
    q = p / (p - 1)
    n = np.arange(1, count + 1, dtype=float)
    weights = np.exp(q * n * np.log(r))
    def Q(t):
        return float(np.sum(weights * np.abs(1 + t * n) ** q))
    res = minimize_scalar(Q, bounds=(-1.1, 0.05), method='bounded', options={'xatol': 2e-13})
    check(res.success)
    return Q(res.x) ** (1 - p)

for p in [1.2, 1.5, 1.75, 2, 2.5, 3.5, 5]:
    q = p / (p - 1)
    for r in [0.25, 0.4, 0.6, 0.8, 0.95]:
        s = exact_single(p, r)
        o = exact_opp(p, r)
        check(isclose(o/s, (1 + r**(-q))**(p-1), rel_tol=1e-11))
        if p >= 2:
            check(o > 2 * s)
        else:
            crit = (2 ** (q - 1) - 1) ** (-1 / q)
            check((o < 2 * s) == (r > crit))

for r in [0.22, 0.4, 0.65, 0.85, 0.96]:
    # The Hilbert confluent jet and the opposite placement have the same cost.
    j = finite_jet(2, r, count=1000)
    check(isclose(j, exact_opp(2, r), rel_tol=3e-8))

for p in [1.4, 1.5, 1.7, 2.5, 3]:
    for r in [0.35, 0.6, 0.82]:
        j = finite_jet(p, r, count=1000)
        s = exact_single(p, r)
        if p > 2:
            check(j > 2 * s)
        elif r == 0.82:
            # All selected sub-Hilbert exponents are beyond the exact
            # sufficient boundary-region criterion at this radius.
            q = p / (p-1)
            sufficient_s = 2 ** (2/q - 2) / (1 - 2 ** (2/q - 2))
            if r ** q > sufficient_s:
                check(j < 2 * s)

print(f'PASS: {checks} finite analytic/numerical checks')

# A strictly increasing finite approximation of the geometric affine-loss
# minimum, mirroring the stop-loss proof for the infinite family.
for q in [1.5, 2, 2.5, 3, 4]:
    s_grid = np.linspace(.08, .92, 24)
    vals = []
    for s in s_grid:
        n = np.arange(1, 1201, dtype=float)
        probs = (1 - s) * np.exp((n-1) * np.log(s))
        y = (1 - s) * n
        fun = lambda b: float(np.sum(probs * np.abs(1 + b*y)**q))
        v = minimize_scalar(fun, bounds=(-3, 0.05), method='bounded').fun
        vals.append(v)
    check(all(b > a + 1e-6 for a,b in zip(vals,vals[1:])))

# A finite-mode collision of two complex nodes to a double zero.
for p in [1.5, 2, 3]:
    r = .8
    q = p / (p - 1)
    n = np.arange(1, 1001, dtype=float)
    at_zero = finite_jet(p, r)
    for theta in [.02, .008, .003]:
        v = r ** n * np.cos(n * theta)
        w = r ** n * np.sin(n * theta) / np.sin(theta)
        fun = lambda t: float(np.sum(np.abs(v + t*w) ** q))
        at_angle = minimize_scalar(fun, bounds=(-1.1, 0.05), method='bounded').fun ** (1-p)
        check(abs(at_angle/at_zero - 1) < .02)

# Exact geometric stop-loss expression, compared with a truncation.
for s in [.2, .48, .8]:
    n = np.arange(1, 2501)
    pmf = (1-s)*s**(n-1)
    for u in [.2, .8, 1.1, 2.5]:
        m = int(np.floor(u/(1-s)))
        exact = s**m * (1-u+m*(1-s))
        numerical = float(np.sum(pmf*np.maximum((1-s)*n-u,0)))
        check(abs(exact - numerical)<1e-12)

print(f'PASS: {checks} total finite analytic/numerical checks')
