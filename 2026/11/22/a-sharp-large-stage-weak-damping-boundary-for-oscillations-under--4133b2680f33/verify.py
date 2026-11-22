#!/usr/bin/env python3
"""Finite numerical cross-checks of the exact stage transfer and asymptotic wave amplification."""
import cmath
import math

checks = 0

def coefficients(s):
    gamma = 1/(s + 1 + math.sqrt(s*s - 1))
    delta = 1/math.sqrt(s*s - 1)
    return gamma, delta

def transfer(s, z):
    gamma, delta = coefficients(s)
    q = (1 + (delta-gamma)*z)/(1-gamma*z)
    c = math.sqrt(s*s-1)/s
    return (1-c) + c*q**s

def stages(s, z):
    gamma, delta = coefficients(s)
    previous = 0j
    total = 0j
    for _ in range(s):
        v = (1 + z*delta*previous)/(1-z*gamma)
        total += v
        previous += v
    return 1 + z*total/s

def profile(omega):
    return omega*omega/2 + math.cos(omega) - 1

for s in (2,3,4,5,8,16,32,64,128):
    for z in (0.5j, 1j, 2j, -1, -3+1j):
        actual = stages(s,z)
        expected = transfer(s,z)
        assert abs(actual-expected) < 2e-11*(1+abs(expected)), (s,z,actual,expected)
        checks += 1

for w in (0.5,1.0,2.0,4.0):
    f = profile(w)
    assert f > 0
    for eta in (0, f/4, f, 2*f):
        previous_err = None
        for s in (64,128,256):
            z = -eta/(s*s) + 1j*w
            val = abs(transfer(s,z))**2
            approximation = f-2*eta
            err = abs(s*s*(val-1)-approximation)
            assert err < 300/(s*s), (s,w,eta,err)
            if previous_err is not None:
                assert err < previous_err/2+1e-8, (s,w,eta,err,previous_err)
            previous_err=err
            if eta==0:
                assert val > 1
            if eta >= f:
                assert val < 1
            checks += 1

for w in (0.5, 1, 2, 4):
    s=512
    f=profile(w)
    energy=abs(transfer(s,1j*w))**(2*int(s*s))
    assert abs(math.log(energy)-f)<1e-4, (w,energy,f)
    checks+=1

print('VERIFY_OK', checks)
