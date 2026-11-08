#!/usr/bin/env python3
"""Independent finite and asymptotic numerical checks for three-rank order/chain width formulas.

Uses only NumPy and the Python standard library. Numerical evidence does not replace the proof.
"""
import itertools
import math
import numpy as np

SEED = 34019
rng = np.random.default_rng(SEED)


def explicit_support(g, m, kind):
    best = -math.inf
    for bits in itertools.product((0, 1), repeat=3*m):
        v = np.asarray(bits, dtype=int).reshape(3, m)
        if kind == 'order':
            admissible = (not v[0].any() or (v[1].all() and v[2].all())) and (not v[1].any() or v[2].all())
        else:
            admissible = sum(bool(v[i].any()) for i in range(3)) <= 1
        if admissible:
            best = max(best, float(np.dot(g, np.asarray(bits))))
    return best


def formula_support(g, m, kind):
    g = np.asarray(g).reshape(3, m)
    positive = np.maximum(g, 0).sum(axis=1)
    if kind == 'chain':
        return float(max(positive))
    total = g.sum(axis=1)
    return float(max(positive[2], total[2]+positive[1], total[2]+total[1]+positive[0]))


for m in (1, 2, 3):
    for _ in range(36):
        g = rng.normal(size=3*m)
        for kind in ('order', 'chain'):
            direct = explicit_support(g, m, kind)
            reduced = formula_support(g, m, kind)
            assert math.isclose(direct, reduced, abs_tol=1e-11), (m, kind, direct, reduced)

pi = math.pi
v = 1-2/pi
a = 1-1/pi
b = 2-1/pi
expected_chain = 3*math.sqrt(a)/(2*math.sqrt(2*pi))
expected_order = (2*math.sqrt(a)+math.sqrt(b))/(2*math.sqrt(2*pi))
expected_gap = (math.sqrt(b)-math.sqrt(a))/(2*math.sqrt(2*pi))
assert expected_order > expected_chain > 0
assert math.isclose(expected_order-expected_chain, expected_gap, abs_tol=1e-14)

# Numerically check the Gaussian maxima formula directly, without using any original geometry.
Z = rng.standard_normal((210000,3))
B = rng.standard_normal((210000,3))*math.sqrt(v)
Y = 0.5*(Z+B)
order_limit = np.maximum.reduce((Y[:,0], Z[:,0]+Y[:,1], Z[:,0]+Z[:,1]+Y[:,2]))
chain_limit = Y.max(axis=1)
assert abs(order_limit.mean()-expected_order) < .015
assert abs(chain_limit.mean()-expected_chain) < .015
assert abs((order_limit-chain_limit).mean()-expected_gap) < .015

# Check the asymptotic gap against an independently simulated finite product-normal model.
m, n = 240, 24000
sums = np.empty((n,3))
totals = np.empty((n,3))
for start in range(0,n,800):
    stop=min(start+800,n)
    z=rng.standard_normal((stop-start,3,m))
    sums[start:stop] = np.maximum(z,0).sum(axis=2)
    totals[start:stop] = z.sum(axis=2)
finite_o=np.maximum.reduce((sums[:,2],totals[:,2]+sums[:,1],totals[:,2]+totals[:,1]+sums[:,0]))
finite_c=sums.max(axis=1)
finite_gap=float(np.mean(finite_o-finite_c)/math.sqrt(m))
assert abs(finite_gap-expected_gap)<.030,(finite_gap,expected_gap)

# The dimension-normalized spherical width gap is the Gaussian gap divided by the chi mean.
const = (math.sqrt(b)-math.sqrt(a))/math.sqrt(6*pi)
assert 0.105<const<0.112
radial_mean=math.sqrt(2)*math.exp(math.lgamma((3*m+1)/2)-math.lgamma(3*m/2))
spherical_gap=2*float(np.mean(finite_o-finite_c))/radial_mean
assert abs(spherical_gap-const)<.035,(spherical_gap,const)

print('THREE_RANK_ORDER_CHAIN_MEAN_WIDTH_CHECKS_PASSED')
print('theoretical_gaussian_sqrt_m_gap',round(expected_gap,10))
print('theoretical_spherical_mean_width_gap',round(const,10))
print('sample_finite_gaussian_sqrt_m_gap',round(finite_gap,10))
print('sample_finite_spherical_gap',round(spherical_gap,10))
