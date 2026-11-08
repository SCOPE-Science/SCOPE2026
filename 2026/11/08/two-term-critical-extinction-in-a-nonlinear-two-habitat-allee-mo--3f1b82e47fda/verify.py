#!/usr/bin/env python3
"""Exact checks and finite numerical sanity tests for a two-habitat nonlinear ODE.

The infinite-time statements require the analytic argument in RESULT.md.
No external dependencies are required.
"""
from fractions import Fraction as F
from math import sqrt


def field(u, v, s, delta, h, m):
    B = s * delta / (s + delta)
    return (u * (u / (m + u) - B - h*u + delta*(v-u)),
            v * (s*(1-v) + delta*(u-v)))


def check_exact():
    cases = [
        (F(1), F(1), F(1,2)),
        (F(1,2), F(1,3), F(2)),
        (F(2,3), F(2,5), F(1,3)),
        (F(1), F(3,2), F(1,5)),
        (F(3,2), F(2), F(1)),
        (F(5,3), F(1,4), F(7,5)),
    ]
    positives = [F(1,9), F(1,3), F(1), F(7,4), F(11,3), F(31,7)]
    checks = 0
    for s, delta, h in cases:
        c = delta / (s+delta)
        B = s*c
        assert 0 < B < 1
        H = h+B
        mc = 1/H
        v0 = s/(s+delta)
        for m in [mc/2, mc, 2*mc]:
            a = 1/m-H
            for u in positives:
                for v in positives:
                    fu, fv = field(u, v, s, delta, h, m)
                    z = v-v0-c*u
                    # Exact derivative of weighted log-population.
                    assert fu/u + c*fv/v == u/(m+u)-H*u
                    # Exact triangularized vector field.
                    assert fu == a*u*u -u**3/(m*(m+u))+delta*u*z
                    assert fv-c*fu == -( (s+delta)*v+c*delta*u )*z -c*a*u*u+c*u**3/(m*(m+u))
                    checks += 3
            if m < mc:
                ue = mc-m
                ve = v0+c*ue
                assert field(ue, ve, s, delta, h, m) == (F(0),F(0))
                checks += 1
        # Coefficients in the exact critical transformed field.
        m = mc
        alpha = 1/m**2
        k3 = c/(s*m**2)
        beta = 1/m**3 +delta*k3
        second = beta/(2*alpha**2)
        assert -s*k3+c/m**2 == 0
        assert beta == 1/m**3 +delta**2/(s*(s+delta)*m**2)
        assert second == m/2+delta**2*m**2/(2*s*(s+delta))
        checks += 3
    return checks


def rk4(m, t_end, dt=0.2):
    # Normalized exact-parameter example: s=delta=1, h=e=1/2.
    u,v = 0.7,0.8
    def fun(x,y):
        return (x*(x/(m+x)-.5-.5*x+(y-x)),y*((1-y)+(x-y)))
    n = round(t_end/dt)
    assert abs(n*dt-t_end)<1e-9
    for _ in range(n):
        a,b=fun(u,v)
        c,d=fun(u+dt*a/2,v+dt*b/2)
        e,f=fun(u+dt*c/2,v+dt*d/2)
        g,h=fun(u+dt*e,v+dt*f)
        u += dt*(a+2*c+2*e+g)/6
        v += dt*(b+2*d+2*f+h)/6
        assert u>0 and v>0
    return u,v


def check_numerical():
    # Finite-time checks illustrate but do not prove limiting conclusions.
    u,v=rk4(0.5,150)
    assert abs(u-0.5)<1e-6 and abs(v-0.75)<1e-6
    t=10000.
    u,v=rk4(1.,t)
    A=1/sqrt(2*t)
    assert abs((u-A)*t-0.75)<0.015
    assert abs((v-.5-.5*A)*t-.375)<0.01
    u,v=rk4(2.,t)
    assert abs(t*u-2)<0.01 and abs(t*(v-.5)-1)<0.01
    return 6


if __name__ == '__main__':
    n=check_exact()
    k=check_numerical()
    print(f'VERIFY_OK: {n} exact rational identities/coefficient checks; {k} numerical-limit sanity checks')
