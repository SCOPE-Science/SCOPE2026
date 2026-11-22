#!/usr/bin/env python3
"""Separate numerical diagnostics for a three-sample Gaussian point-source regression.

The continuum assertions are established in RESULT.md; this file checks algebra,
limiting signs, and representative numerical geometry, not universal proofs.
"""
import math
from scipy.optimize import minimize_scalar, brentq
import numpy as np

checks = 0

def assert_close(u, v, atol=1.e-10, rtol=1.e-10):
    global checks
    checks += 1
    assert math.isclose(u, v, abs_tol=atol, rel_tol=rtol), (u, v)

def assert_true(v):
    global checks
    checks += 1
    assert v

def matrix(x, d):
    return np.array([[math.exp(-.5*(x+d)**2), math.exp(-.5*(x-d)**2), 1.],
                     [math.exp(-.5*d*d), math.exp(-.5*d*d), 1.],
                     [math.exp(-.5*(x-d)**2), math.exp(-.5*(x+d)**2), 1.]])

def oriented_det(x, d):
    a = math.exp(-.5*(x-d)**2)
    b = math.exp(-.5*(x+d)**2)
    c = math.exp(-.5*d*d)
    return (a-b)*(a+b-2*c)

def f(x,d):
    return math.exp(-.5*x*x)*math.cosh(d*x)

def singular_width(d):
    assert d>1
    return brentq(lambda x:f(x,d)-1,1.e-4,max(4.,3*d),xtol=1.e-13)

def branch_peaks(d):
    z = singular_width(d)
    u = minimize_scalar(lambda x:-oriented_det(x,d),bounds=(1.e-7,z),method='bounded',options={'xatol':1.e-13})
    v = minimize_scalar(lambda x:oriented_det(x,d),bounds=(z,z+max(5,2*d+2)),method='bounded',options={'xatol':1.e-13})
    return z,u.x,-u.fun,v.x,-v.fun

for d in [.01,.1,.4,.9,1.,1.001,1.01,1.25,1.3,1.4,1.6,2.,5.]:
    for x in [.02,.2,.6,1.,2.,4.,8.]:
        u = matrix(x,d)
        assert_close(abs(np.linalg.det(u)),abs(oriented_det(x,d)),atol=2.e-12)
        assert_close(np.linalg.det(u.T@u),np.linalg.det(u)**2,atol=2.e-10,rtol=5.e-8)
        if d<=1:
            assert_true(oriented_det(x,d)<0)
    if d>1:
        z,ul,l,ur,r = branch_peaks(d)
        assert_true(0 < ul < z < ur)
        assert_true(l>0 and r>0)
        assert_close(f(z,d),1,atol=1.e-12)
        assert_close(oriented_det(z,d),0,atol=1.e-12)
        for t in [.01,.2,.5,.9]:
            assert_true(oriented_det(z*t,d)>0)
        for t in [.01,.2,1.,2.]:
            assert_true(oriented_det(z+t,d)<0)

rstar = brentq(lambda d:branch_peaks(d)[2]-branch_peaks(d)[4],1.2,1.5,xtol=1.e-13)
z, xl, left, xr, right = branch_peaks(rstar)
assert_close(left,right,atol=1.e-10)
assert_true(1 < xl < z < xr)
for d in [1.05,1.15,1.2,1.25]:
    z, xl, left, xr, right=branch_peaks(d)
    assert_true(left<right)
for d in [1.35,1.5,2,3]:
    z, xl, left, xr, right=branch_peaks(d)
    assert_true(left>right)
print('diagnostic_checks_passed',checks)
print('numerical_equal_peak_separation_d',format(rstar,'.13f'))
print('inner_optimum_x',format(xl if False else branch_peaks(rstar)[1],'.13f'))
print('outer_optimum_x',format(branch_peaks(rstar)[3],'.13f'))
print('squared_design_determinant_at_equal_peaks',format(left*left if False else branch_peaks(rstar)[2]**2,'.13f'))
print('Important: numerical root is illustrative, existence proved analytically, uniqueness of tie not claimed')
