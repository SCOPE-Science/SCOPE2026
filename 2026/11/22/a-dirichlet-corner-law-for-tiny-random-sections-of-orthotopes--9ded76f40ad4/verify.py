#!/usr/bin/env python3
"""Supplementary numerical and symbolic checks for orthotope small-slice laws.

No stochastic assertions are used as proof of an infinite-dimensional statement.
"""
import math
from itertools import combinations
import numpy as np
import mpmath as mp
from scipy.stats import qmc, norm


def leading_constant(d, sides):
    assert d >= 2 and len(sides) == d and min(sides) > 0
    d = mp.mpf(d)
    q = (d-1)
    a = d/(2*q)
    return 2*mp.factorial(int(q))**(1/q) * mp.gamma((d+1)/2) * mp.gamma(a)**int(d) / (mp.pi**(q/2) * mp.gamma(d*a)*sum(map(mp.mpf,sides)))


def sectional_area_3d(s, n, sides):
    """Separate cubic-box-spline section-area calculation (s from a vertex)."""
    b = n * np.asarray(sides)
    val = s*s
    for i in range(3):
        val = val - np.maximum(s-b[:,i],0)**2
    for i,j in combinations(range(3),2):
        val = val + np.maximum(s-b[:,i]-b[:,j],0)**2
    val = val - np.maximum(s-b.sum(axis=1),0)**2
    return val / (2*np.prod(n,axis=1))


def qmc_tail_coefficient_3d(sides, eps, power=15):
    xy=qmc.Sobol(2, scramble=False).random_base2(power)
    # The octant of the sphere has constant area in (z,phi) variables.
    z=xy[:,0]
    phi=(math.pi/2)*xy[:,1]
    rr=np.sqrt(1-z*z)
    n=np.column_stack([rr*np.cos(phi),rr*np.sin(phi),z])
    # Avoid the Sobol endpoint on an axis, a measure-zero orientation.
    n=n[np.all(n>1.e-14,axis=1)]
    w=n@np.asarray(sides,dtype=float)
    lo=np.zeros(len(n)); hi=w/2
    assert np.min(sectional_area_3d(hi,n,sides))>eps
    for _ in range(43):
        m=(lo+hi)/2
        a=sectional_area_3d(m,n,sides)
        hi=np.where(a>eps,m,hi)
        lo=np.where(a<=eps,m,lo)
    # Direction's full support has two symmetric endpoint intervals.
    return float(np.mean(2*hi)/np.mean(w)/math.sqrt(eps))


def angular_moments(d,power=16):
    U=qmc.Sobol(d,scramble=True,seed=20261121).random_base2(power)
    Z=norm.ppf(np.clip(U,1e-14,1-1e-14))
    Z/=np.linalg.norm(Z,axis=1)[:,None]
    alpha=1/(d-1)
    wt=np.prod(np.abs(Z)**alpha,axis=1)
    X=Z*Z
    return [float(np.sum(wt*X[:,0]**2)/wt.sum()),float(np.sum(wt*X[:,0]*X[:,1])/wt.sum())]


def run():
    mp.mp.dps=45
    assert mp.almosteq(leading_constant(2,[1,2]),mp.mpf(1)/3,rel_eps=mp.mpf('1e-43'))
    K3=leading_constant(3,[1,1,1])
    exact=2*mp.sqrt(2)*mp.gamma(mp.mpf(3)/4)**3/(3*mp.pi*mp.gamma(mp.mpf(9)/4))
    assert mp.almosteq(K3,exact,rel_eps=mp.mpf('1e-43'))
    assert abs(float(K3)-0.4874096864474279)<1e-14
    for d in range(2,9):
        c=leading_constant(d,[1]*d)
        assert c>0
        unequal=[float(i+1) for i in range(d)]
        cu=leading_constant(d,unequal)
        assert mp.almosteq(cu/c,mp.mpf(d)/sum(unequal),rel_eps=mp.mpf('1e-40'))
    for sides in ([1.,1.,1.],[1.,2.,3.]):
        theory=float(leading_constant(3,sides))
        values=[]
        for eps in [0.01,0.001,0.0001]:
            v=qmc_tail_coefficient_3d(sides,eps,power=15)
            values.append(v)
        assert abs(values[-1]/theory-1)<0.015,(sides,theory,values)
        assert abs(values[-1]-theory)<=abs(values[0]-theory)+0.002,(sides,theory,values)
        print('3d_box',sides,'theoretical',theory,'numerical_by_epsilon',values)
    for d in (3,4):
        observed=angular_moments(d)
        a=d/(2*(d-1)); total=d*a
        expected=[a*(a+1)/(total*(total+1)),a*a/(total*(total+1))]
        assert np.allclose(observed,expected,atol=0.013,rtol=0)
        print('Dirichlet_moments',d,'numeric',observed,'theory',expected)
    print('PASS; exact gamma identities, box-spline tests, weighted angular moments')

if __name__=='__main__':run()
