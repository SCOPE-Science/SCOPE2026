#!/usr/bin/env python3
"""Independent numerical checks of the exact first-cut-locus distance law on L(5,2)."""
import math
import numpy as np
import mpmath as mp

mp.mp.dps = 65
pi = mp.pi
a = pi / 5
b = mp.acos(-mp.mpf(1) / 4) / 2
c1 = mp.cos(2 * pi / 5)
c2 = mp.cos(4 * pi / 5)
delta = c1 - c2
v = 2 * pi**2 / 5

def sphere_cdf(r):
    return 5 / pi * (r - mp.sin(r) * mp.cos(r))

def exact_cdf(r):
    if r < a:
        return sphere_cdf(r)
    if r > b:
        raise ValueError('outside proved range')
    B = ((r - a) * (1 + mp.cos(2*a) + mp.cos(2*r))
         + mp.sin(2*a) - mp.sin(2*r) - mp.sin(2*(r-a)) / 2)
    return sphere_cdf(r) - 20 / (pi * mp.sqrt(5)) * B

def overlap_volume(r,d):
    if d >= 2*r:
        return mp.mpf('0')
    return 2*pi*(r - d/2 - mp.cos(r)**2 * (mp.tan(r) - mp.tan(d/2)))

def integral_cdf(r):
    if r<=a:
        return sphere_cdf(r)
    deficit = 2/delta * mp.quad(lambda d: overlap_volume(r,d)*mp.sin(d), [2*a,2*r])
    return sphere_cdf(r) - deficit/v

rs = [mp.mpf(s) for s in ['0.3','0.6','0.65','0.7','0.8','0.9']]
for r in rs:
    val = exact_cdf(r)
    direct = integral_cdf(r)
    assert abs(val - direct) < mp.mpf('1e-55'), (r, val, direct)

K = 10*(mp.sqrt(5)-1)/(3*pi)
for eps in [mp.mpf('0.01'),mp.mpf('0.002'),mp.mpf('0.0005'),mp.mpf('0.0001')]:
    ratio = (sphere_cdf(a+eps)-exact_cdf(a+eps))/(eps**3)
    assert abs(ratio/K-1)<4*eps, (eps,ratio,K)

# Independent Haar-pair simulation, using complex coordinates of S^3 and quotient orbit distances.
rng = np.random.default_rng(20261105)
N = 2_000_000
counts = np.zeros(len(rs), dtype=np.int64)
total_distance = 0.0
zeta = np.exp(2j*np.pi*np.arange(5)/5)
thresholds = np.cos(np.array([float(r) for r in rs]))
for count in [200_000]*10:
    x = rng.normal(size=(count,4))
    y = rng.normal(size=(count,4))
    x /= np.linalg.norm(x,axis=1,keepdims=True)
    y /= np.linalg.norm(y,axis=1,keepdims=True)
    x1 = x[:,0]+1j*x[:,1]
    x2 = x[:,2]+1j*x[:,3]
    y1 = y[:,0]+1j*y[:,1]
    y2 = y[:,2]+1j*y[:,3]
    h1 = np.conjugate(x1)*y1
    h2 = np.conjugate(x2)*y2
    m = np.full(count,-2.0)
    for k in range(5):
        dot = (h1*zeta[k]+h2*zeta[(2*k)%5]).real
        m = np.maximum(m,dot)
    counts += np.count_nonzero(m[:,None]>=thresholds[None,:],axis=0)
    total_distance += np.arccos(np.clip(m,-1,1)).sum()
for r,n in zip(rs,counts):
    obs = n/N
    expect = float(exact_cdf(r))
    sigma = math.sqrt(expect*(1-expect)/N)
    assert abs(obs-expect)<6*sigma+0.0002,(r,obs,expect,sigma)
    print(f'radius={float(r):.6f} exact={expect:.9f} sampled={obs:.9f} z={(obs-expect)/sigma:+.2f}')
print('mean_sampled_distance',total_distance/N)
print('K',mp.nstr(K,28),'cut_radius',mp.nstr(a,24),'end_of_exact_window',mp.nstr(b,24))
print(f'LENSSPACE_FIRST_CUT_LOCUS_LAW_OK samples={N} quadrature_tests={len(rs)}')
