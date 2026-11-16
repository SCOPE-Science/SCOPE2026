#!/usr/bin/env python3
"""Numerical consistency tests for SU(2) conjugacy-class Fourier multipliers.

The global theorem is analytical; these tests are supplemental only.
"""
import math

def normalized_character(m, theta):
    if theta == 0:
        return 1.0
    if theta == math.pi:
        return (-1.0) ** m
    return math.sin((m+1)*theta) / ((m+1)*math.sin(theta))

def finite_radius(theta, maximum_degree=2000):
    return max(abs(normalized_character(m,theta)) for m in range(1,maximum_degree+1))

def run():
    tests=0
    for sign in (-1,1):
        c=sign/4
        theta=math.acos(c)
        lambdas=[normalized_character(m,theta) for m in range(1,25001)]
        assert abs(lambdas[0]-c)<1e-13; tests+=1
        assert abs(lambdas[1]+0.25)<1e-13; tests+=1
        assert abs(abs(lambdas[2])-7/32)<1e-13; tests+=1
        assert abs(lambdas[3]-1/16)<1e-13; tests+=1
        assert abs(max(map(abs,lambdas))-0.25)<1e-12; tests+=1
        assert all(abs(x)<0.25-1e-12 for x in lambdas[2:]); tests+=1
        assert abs(math.sin(theta)-math.sqrt(15)/4)<1e-13; tests+=1
        assert 4/(5*math.sqrt(15))<1/4; tests+=1
        for k in (1,2,3,5,10):
            assert abs(max(abs(v)**k for v in lambdas)-4**(-k))<1e-12
            tests+=1
    for j in range(1,1000):
        theta=math.pi*j/1000
        c=abs(math.cos(theta))
        lower=max(c, abs(4*c*c-1)/3)
        assert lower >= .25-1e-13; tests+=1
        assert finite_radius(theta, maximum_degree=400) >= lower-1e-13; tests+=1
    # SU(2) and SO(3) differ: the spin-one-half (m=1) sector is absent after quotient.
    for m in range(1,1500):
        theta=math.acos(0.25)
        val=normalized_character(m,theta)
        symmetry=normalized_character(m,math.pi-theta)
        assert abs(symmetry-((-1)**m)*val)<2e-12; tests+=1
    print('PASS',tests,'checks: low irreps, tail, angle uniqueness, powers, center parity')

if __name__=='__main__':
    run()
