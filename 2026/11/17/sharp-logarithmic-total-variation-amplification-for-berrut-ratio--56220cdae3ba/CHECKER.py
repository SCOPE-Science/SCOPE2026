#!/usr/bin/env python3
"""Standalone arithmetic and numerical spot checks for equispaced Berrut interpolation.
Analytical asymptotic claims are proved separately; sampling is not a proof."""
from fractions import Fraction
import math
import numpy as np


def alt(q, z):
    return sum(((-1)**j) / (z + j) for j in range(q))


def rat(x, values):
    n = len(values) - 1
    for j in range(n + 1):
        if x == j:
            return values[j]
    a = [Fraction((-1)**j, 1) / (x - j) for j in range(n + 1)]
    return sum(a[j] * values[j] for j in range(n + 1)) / sum(a)


exact = 0
for n in range(2, 20):
    for m in range(n):
        t = Fraction(2, 5)
        x = m + t
        s = alt(m + 1, t) + alt(n - m, 1 - t)
        d = sum(Fraction((-1)**j, 1) / (x - j) for j in range(n + 1))
        assert d == (-1)**m * s
        for k in range(1, n+1):
            data = [int(j >= k) for j in range(n + 1)]
            rr = rat(x, data)
            if m < k:
                expected = Fraction((-1)**(k+m+1),1) * alt(n-k+1,k-x)/s
            else:
                expected = 1-Fraction((-1)**(k+m-1),1)*alt(k,x-k+1)/s
            assert rr == expected
            exact += 1
print('EXACT_BARYCENTRIC_ALTERNATING_STEP_IDENTITIES_PASS', exact)


def grid_interp(data, intervals_per_cell=120):
    n = len(data)-1
    grid = np.linspace(0., float(n), n*intervals_per_cell+1)
    pts = np.arange(n+1)
    w = (-1.)**pts
    at_knots = np.isclose(grid, np.round(grid), atol=1e-12)
    y = np.empty(len(grid))
    y[at_knots] = data[np.rint(grid[at_knots]).astype(int)]
    z = grid[~at_knots]
    a = w[None,:]/(z[:,None]-pts[None,:])
    y[~at_knots] = (a @ data)/a.sum(axis=1)
    return y

for n in [8,16,32,64,128]:
    v = []
    for k in (1, (n+1)//2, n):
        data = np.array([int(j>=k) for j in range(n+1)], dtype=float)
        y = grid_interp(data, 100)
        vv = float(np.abs(np.diff(y)).sum())
        assert abs(vv-2/math.pi*math.log(n)) < 2.5
        v.append(vv)
    assert v[0] > (2/math.pi)*math.log(n)-1
    print('STEP_VARIATION_LOG_SCALE_NUMERICAL',n,*[f'{x:.7f}' for x in v])

rng=np.random.default_rng(41731)
for n in [4,8,16]:
    steps = [grid_interp(np.array([int(j>=k) for j in range(n+1)],float)) for k in range(1,n+1)]
    for z in range(15):
        data=rng.standard_normal(n+1)
        reconstruction = data[0] + sum((data[k]-data[k-1])*steps[k-1] for k in range(1,n+1))
        direct = grid_interp(data)
        assert np.max(np.abs(reconstruction-direct))<1e-11
        direct_v=np.sum(np.abs(np.diff(direct)))
        upper=sum(abs(data[k]-data[k-1])*np.sum(np.abs(np.diff(steps[k-1]))) for k in range(1,n+1))
        assert direct_v <= upper+1e-10
print('JUMP_DECOMPOSITION_AND_TRIANGLE_VARIATION_PASS')
print('ALL_BERRUT_VARIATION_SPOT_CHECKS_PASS')
