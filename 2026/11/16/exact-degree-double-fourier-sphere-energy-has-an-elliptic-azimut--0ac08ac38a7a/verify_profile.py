#!/usr/bin/env python3
"""Independent finite checks of latitude-coordinate spherical-harmonic energy.
All normalizations and integrals are explicit; this is not an infinite proof.
"""
from math import pi, comb, log
import numpy as np
from scipy.special import sph_harm_y, ellipk
from scipy.integrate import simpson

def energy(l, m, size=6001):
    th=np.linspace(0., pi, size)
    y=sph_harm_y(l, m, th, np.zeros_like(th))
    return float(4*simpson(np.abs(y)**2, x=th))

def exact_zonal(l):
    a=[comb(2*j,j)/4**j for j in range(l+1)]
    return (2*l+1)*sum((a[j]*a[l-j])**2 for j in range(l+1))

def exact_sectoral(l):
    return (2*l+1)*(comb(2*l,l)/4**l)**2

count=0
for l in range(0,45):
    vals=[]
    for m in range(l+1):
        v=energy(l,m)
        vals.append(v)
        assert v>0 and np.isfinite(v)
        count+=1
    assert abs(vals[0]-exact_zonal(l))<2e-9, (l, vals[0], exact_zonal(l))
    assert abs(vals[-1]-exact_sectoral(l))<2e-9, (l, vals[-1], exact_sectoral(l))
    count+=2
for alpha in [.25,.5,.8,1.]:
    target=4/pi**2*ellipk(1-alpha**2)
    data=[energy(l, round(alpha*l), 8001) for l in (80,120,180)]
    assert abs(data[-1]-target)<.065,(alpha,target,data)
    print('elliptic_profile',alpha,'target',round(target,9),'observations',*[round(d,9) for d in data])
    count+=4
for l in [20,40,80,160]:
    print('zonal',l,'energy',round(exact_zonal(l),9),'leading_log',round((4/pi**2)*log(l),9),'sectoral',round(exact_sectoral(l),9))
    count+=2
print('PASS',count,'checks')
