"""Independent numerical checks of the spherical-triangle maximal-perimeter limit.
Run: python check.py  (NumPy and SciPy required).
The Monte Carlo checks are finite diagnostics, not proofs.
"""
import numpy as np
from scipy.special import gamma
from numpy.polynomial.legendre import leggauss

C = 3 * np.pi * gamma(0.75) / gamma(0.25)**3

def integration(n):
    x,w=leggauss(n)
    a=np.pi*(x+1)/2
    wa=w*np.pi/2
    u=a[:,None]*(x[None,:]+1)/2
    wu=a[:,None]*w[None,:]/2
    kern=np.sqrt(np.maximum(0,np.sin(a[:,None])*np.sin(u)*np.sin(a[:,None]-u)))
    I=np.sum(wa[:,None]*wu*kern)
    # Weighted expected first geodesic side length
    avg_a=np.sum(wa[:,None]*wu*kern*a[:,None])/I
    return np.sqrt(2)*I/(4*np.pi),avg_a

c1,m1=integration(200)
c2,m2=integration(400)
assert abs(c2-C)<4e-7,(c2,C)
assert abs(c1-c2)<5e-7,(c1,c2)

rng=np.random.default_rng(771)
N=8_000_000
thresholds=[0.04,0.015,0.006]
counts=np.zeros(len(thresholds),dtype=np.int64)
a_sums=np.zeros(len(thresholds))
ratio_sums=np.zeros(len(thresholds))
ratio_half=np.zeros(len(thresholds))
for _ in range(N//400000):
    a=np.arccos(rng.uniform(-1,1,400000))
    theta=rng.uniform(0,2*np.pi,400000)
    lat=np.arcsin(rng.uniform(-1,1,400000))
    k=np.cos(lat)
    d1=np.arccos(np.clip(k*np.cos(theta),-1,1))
    d2=np.arccos(np.clip(k*np.cos(theta-a),-1,1))
    deficit=2*np.pi-(a+d1+d2)
    for j,eps in enumerate(thresholds):
        sel=(deficit<eps)
        counts[j]+=np.count_nonzero(sel)
        a_sums[j]+=np.sum(a[sel])
        ratio_sums[j]+=np.sum(deficit[sel]/eps)
        ratio_half[j]+=np.sum(deficit[sel]/eps<.25)

for eps,n,aa,rr,ff in zip(thresholds,counts,a_sums,ratio_sums,ratio_half):
    estimate=n/N/np.sqrt(eps)
    print('epsilon',eps,'n',n,'tail',estimate,'target',C,
          'mean_first_side',aa/n,'target',m2,
          'mean_scaled_deficit',rr/n,'target',1/3,
          'cdf_quarter',ff/n,'target',.5)
assert abs((counts[-1]/N/np.sqrt(thresholds[-1]))-C)<0.01
assert abs(a_sums[-1]/counts[-1]-m2)<0.025
assert abs(ratio_sums[-1]/counts[-1]-1/3)<0.02
assert abs(ratio_half[-1]/counts[-1]-0.5)<0.03
print('SPHERICAL_TRIANGLE_MAX_PERIMETER_MARKED_LAW_OK')
