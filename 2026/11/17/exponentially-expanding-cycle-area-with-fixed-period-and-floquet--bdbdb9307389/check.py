#!/usr/bin/env python3
"""Numerical consistency checks for exact cubic-cycle area identities.

This checks finite test parameters only. The infinite-parameter assertions are
proved analytically in RESULT.md.
"""
from math import pi, exp, cos, sin, factorial


def area_series(lam, a, omega, epsilon, max_terms=130):
    A, B = a/omega, epsilon/omega
    term = 1.0
    total = term
    for n in range(1, max_terms):
        term *= (2*n-1)/(2*n) * B*B/(A*A+n*n)
        total += term
        if abs(term)<1e-15*total:
            break
    return pi*lam/a*total


def periodic_graph(lam, a, omega, epsilon, steps=2000, turns=20):
    # integrate dv/du = lam/omega - (a+epsilon*cos(u))*v/omega.
    du = 2*pi/steps
    def f(u,v): return (lam-(a+epsilon*cos(u))*v)/omega
    v = lam/a
    for i in range(steps*turns):
        u=i*du
        k1=f(u,v)
        k2=f(u+du/2,v+du*k1/2)
        k3=f(u+du/2,v+du*k2/2)
        k4=f(u+du,v+du*k3)
        v += du*(k1+2*k2+2*k3+k4)/6
    first=v
    area_sum=0.0
    period_sum=0.0
    for i in range(steps):
        u=i*du
        area_sum += v
        period_sum += 1/v
        k1=f(u,v)
        k2=f(u+du/2,v+du*k1/2)
        k3=f(u+du/2,v+du*k2/2)
        k4=f(u+du,v+du*k3)
        v += du*(k1+2*k2+2*k3+k4)/6
    # theta=u/2, radial area = integral_0^pi v(u) du / 2
    # since v(u) is 2pi periodic: area = (1/2)*integral_0^2pi v(u) du.
    area=area_sum*du/2
    # physical period = integral_0^4pi 1/(omega*v) du/2;
    # so exactly integral_0^2pi 1/(omega*v) du.
    physical_period=period_sum*du/omega
    return first,v,area,physical_period


def run():
    lam,a,omega=1.2,1.3,0.9
    for eps in [0.0,0.5,1.3,2.7,5.0]:
        first,last,area,period=periodic_graph(lam,a,omega,eps)
        expected_area=area_series(lam,a,omega,eps)
        expected_T=2*pi*a/(lam*omega)
        assert abs(last-first) < 5e-10, (eps,last,first)
        assert abs(area/expected_area-1)<4e-7,(eps,area,expected_area)
        assert abs(period/expected_T-1)<4e-7,(eps,period,expected_T)
    assert abs(area_series(lam,a,omega,0)-pi*lam/a)<1e-12
    assert area_series(lam,a,omega,3)>area_series(lam,a,omega,2)
    assert area_series(lam,a,omega,-3)==area_series(lam,a,omega,3)
    print('CUBIC_ALL_ANISOTROPY_AREA_IDENTITIES_OK')


if __name__=='__main__':
    run()
