#!/usr/bin/env python3
"""Finite numerical checks for a cubic-center occupation theorem.

Python 3 standard library only. The analytic theorem is proved in RESULT.md.
"""
import math


def P(x):
    return 1 + 3*x*x


def U(x):
    p = P(x)
    return (math.log(p) - 2/p + 2)/9


def invariant_derivative(x,y):
    p = P(x)
    ux = 2*x*(1+x*x)/(p*p)
    hx = ux - 6*x*y*y/(p*p)
    hy = 2*y/p
    return hx*(p*y) + hy*(-x-x**3+3*x*y*y)


def width(E):
    lo = max(0,9*E-3)
    hi = 9*E
    for _ in range(90):
        w = (lo+hi)/2
        if w-2*math.exp(-w)+2-9*E > 0:
            hi = w
        else:
            lo = w
    return (lo+hi)/2


def I(q, E, n=18000):
    """Midpoint quadrature in w=W sin^2(theta), removing both square-root ends."""
    W = width(E)
    h = math.pi/(2*n)
    total = 0.0
    for j in range(n):
        theta = (j+0.5)*h
        s = math.sin(theta)
        c = math.cos(theta)
        w = W*s*s
        a = math.expm1(w)/3
        dw = 2*W*s*c
        diff = W-w
        delta = diff + 2*math.exp(-w)*(-math.expm1(-diff))
        integrand = 0.5*(a**((q-1)/2))*math.exp(-w/2)*dw/math.sqrt(delta)
        total += integrand
    return h*total


def check():
    for xi in range(-8,9):
        for yi in range(-8,9):
            x, y = xi/5, yi/7
            assert abs(invariant_derivative(x,y)) < 5e-13
    targets = {"period":4/math.sqrt(3), "second":3.0,
               "third":math.sqrt(math.pi/2)}
    residuals = []
    for E in (1.0, 2.0, 3.0, 5.0):
        J0=I(0,E)
        W=width(E)
        A=math.sqrt(math.expm1(W)/3)
        T=4*J0
        moment1=I(1,E)/J0
        moment2=I(2,E)/J0
        moment3=I(3,E)/J0
        assert abs(I(0,E)/J0-1)<1e-14
        assert T>0 and moment1>0 and moment2>0
        res=(E,T*math.sqrt(E),moment2/E,moment3/(A*math.sqrt(E)))
        residuals.append(res)
        print("E, scaled T, M2/E, M3/(A sqrt E):", *[round(z,9) for z in res])
    assert abs(residuals[-1][1]-targets["period"])<.06
    assert abs(residuals[-1][2]-targets["second"])<.18
    assert abs(residuals[-1][3]-targets["third"])<.04
    assert all(residuals[j][2] < residuals[j+1][2] for j in range(len(residuals)-1))
    print("STUDENT_CUBIC_MOMENT_TRANSITION_OK")


if __name__ == '__main__':
    check()
