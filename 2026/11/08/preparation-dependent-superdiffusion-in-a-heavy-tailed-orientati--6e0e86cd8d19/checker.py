"""Reproducible finite diagnostics for Lomax orientational-renewal transport.

The theoretical long-time statements require the separate mathematical proof.
Run: python checker.py (NumPy required for the fixed-seed count simulations).
"""
import math
import numpy as np


def simpson(f, a, b, n=24000):
    assert n % 2 == 0
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        total += (4 if i & 1 else 2) * f(a + i*h)
    return h*total/3


def renewal_counts(alpha, tau, t, stationary, count=20000, seed=72):
    rng = np.random.default_rng(seed + (1 if stationary else 0))
    remaining = np.full(count, t, dtype=float)
    counts = np.zeros(count, dtype=np.int32)
    if stationary:
        # Exact equilibrium forward residual survival: (1+s/tau)^(1-alpha).
        residual = tau*(np.power(rng.random(count), -1/(alpha-1))-1)
        hit = remaining >= residual
        counts[hit] += 1
        remaining[hit] -= residual[hit]
        remaining[~hit] = -1
    for j in range(12000):
        active = np.flatnonzero(remaining > 0)
        if not len(active):
            break
        intervals = tau*(np.power(rng.random(len(active)), -1/alpha)-1)
        hit = remaining[active] >= intervals
        counts[active[hit]] += 1
        remaining[active[hit]] -= intervals[hit]
        remaining[active[~hit]] = -1
    else:
        raise AssertionError('simulation loop unexpectedly exhausted')
    return float(counts.mean()), float(counts.var())


def run():
    alpha, tau, d, v = 1.5, 1.0, 1.0, 1.0
    mu = tau/(alpha-1)
    c = tau**alpha
    # E(exp(-dT)) from inverse-CDF uniform quadrature.
    laplace = simpson(lambda z: 0 if z==0 else math.exp(-d*tau*(z**(-1/alpha)-1)), 0, 1)
    k = 1-laplace
    # Independent integration-by-parts survival representation for the same mean reward.
    k2 = d*simpson(lambda s: math.exp(-d*s)*(1+s/tau)**(-alpha), 0, 60, n=24000)
    assert abs(k-k2)<1e-8, (k,k2)
    assert abs(k-0.484255687717376)<1e-8
    b0 = 2*c/(mu**3*(2-alpha)*(3-alpha))
    b1 = b0/(alpha-1)
    assert abs(b0-1/3)<1e-13
    assert abs(b1-2/3)<1e-13
    assert abs(b1/b0-2)<1e-13
    physical0 = (v*k/d)**2*b0
    physical1 = (v*k/d)**2*b1
    assert abs(physical0-0.0781678570288762)<1e-8
    assert abs(physical1-0.156335714057752)<1e-8
    print('exact k',k, 'fresh coefficient',physical0,'equilibrium coefficient',physical1)
    # These simulations concern counts, not the exact ABP theorem; wide tolerance is deliberate.
    for stationary in [False, True]:
        mean, variance = renewal_counts(alpha,tau,2000.,stationary,seed=18227)
        predicted = (b1 if stationary else b0)*2000.**(3-alpha)
        assert abs(variance/predicted-1)<0.19, (stationary, variance, predicted)
        if stationary:
            assert abs(mean-2000/mu)<9
        else:
            assert mean>2000/mu
        print('stationary' if stationary else 'fresh','count mean',mean,'count variance',variance,'asymptotic ratio',variance/predicted)
    print('PASS: deterministic constants, independent reward quadratures, seeded finite-count diagnostics')


if __name__ == '__main__':
    run()
