#!/usr/bin/env python3
"""Deterministic tests for reflecting--absorbing passage-profile reconstruction.

Only standard-library Python required. These tests complement, not replace,
the analytic proof of the continuum theorem.
"""
import math


def simpson(func, right, panels=800):
    assert panels % 2 == 0
    h = right / panels
    sm = func(0.0) + func(right)
    for i in range(1, panels):
        sm += (4 if i % 2 else 2) * func(i * h)
    return sm * h / 3


def vp(eta, s):
    return 2 * math.sqrt(1 + eta * s * s) * simpson(
        lambda u: u*u / math.sqrt(1 + eta*u*u), s)


def vpp(eta, s):
    z = math.sqrt(1+eta*s*s)
    integ = vp(eta,s)/(2*z)
    return -2*(eta*s*integ/z+s*s)


def v(eta, x):
    return simpson(lambda y: vp(eta,1-y), x)


def check():
    tests = 0
    for eta in [-0.75, -0.2, 0.0, 0.35, 1.0, 3.0]:
        for x in [0.0,0.12,0.29,0.48,0.77,0.94]:
            s=1-x
            D=1+eta*s*s
            b=eta*s
            a=vp(eta,s)
            a2=vpp(eta,s)
            W=s*a2+a+2*s**3
            assert W>0
            assert abs(a/W-D)<1e-11 * max(1,D)
            assert abs(D*a2+b*a+2*D*s*s)<2e-11
            assert abs(-D+b*s+1)<2e-14
            if eta==0.0:
                assert abs(v(eta,x)-(1-s**4)/6)<2e-12
            tests+=4
    for x in [0.05, 0.2, 0.5, 0.8, 0.98]:
        last=-1
        for eta in [-0.75,-0.2,0.0,0.35,1.0,3.0]:
            z=v(eta,x)
            assert z>last
            last=z
            tests+=1
    # Boundary quartic, and mean-law invariance in the example family.
    for eta in [-0.7,0,2]:
        for s in [0.03,0.02,0.01]:
            ratio=(v(eta,1)-v(eta,1-s))*6/s**4
            assert abs(ratio-1)<0.015
            tests+=1
    print('PASS',tests,'deterministic analytic/numeric family checks')


if __name__=='__main__':
    check()
