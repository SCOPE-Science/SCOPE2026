#!/usr/bin/env python3
"""Reproduce symbolic coefficients and small-amplitude periodic-orbit diagnostics.

The full-period computations are finite consistency checks, not proofs of the
existence, completeness, or asymptotic statements in the accompanying theorem.
"""
import math
import sympy as sp
import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import expit, logit


def response(z, lam):
    w = np.tanh(z / 2)
    return (w + lam * w**3) / (1 + lam)


def orbit(rho, t, a, theta, epsilon, lam):
    xstar = 1 / (1 + theta)
    ustar, vstar = logit(xstar), logit(t)
    def ode(T, z):
        u, v, n_integral, x_integral, n_cube = z
        x = expit(u)
        n = expit(v)
        return [response(a*(t-n), lam),
                epsilon*((1+theta)*x-1), n, x, (n-t)**3]
    def event(T, z):
        return z[0] - ustar
    event.direction = -1
    freq = math.sqrt(a / (2*(1+lam))*t*(1-t)*epsilon*(1+theta)*xstar*(1-xstar))
    sol = solve_ivp(ode, (0, 2.5*2*math.pi/freq),
                    [ustar, vstar+rho, 0, 0, 0],
                    method='DOP853', atol=3e-14, rtol=4e-13,
                    max_step=0.06, dense_output=True, events=event)
    assert sol.success
    periods = [r for r in sol.t_events[0] if r > 1e-5]
    assert periods, 'No full-period event found'
    T = periods[0]
    y = sol.sol(T)
    assert abs(y[0]-ustar) < 2e-10 and abs(y[1]-(vstar+rho)) < 2e-10
    grid = np.linspace(0,T,2001)
    n = expit(sol.sol(grid)[1])
    A = (max(n)-min(n))/2
    return A, y[2]/T-t, y[3]/T-xstar, y[4]/T, T


def symbolic():
    z, lam, t, a, p = sp.symbols('z lam t a p', real=True)
    F = (sp.tanh(z/2)+lam*sp.tanh(z/2)**3)/(1+lam)
    Fp = sp.diff(F,z).subs(z,0)
    Fppp = sp.diff(F,z,3).subs(z,0)
    assert sp.simplify(Fppp/Fp - (3*lam-1)/2) == 0
    # Quadratic logit oscillator: normalized constant/second harmonic pieces.
    p2 = p*(1-2*t)
    a2_over_a0 = p2/(2*p)
    C0 = -a2_over_a0/2
    C2 = a2_over_a0/6
    moment = sp.simplify(3*p**2*(p*(C0/2+C2/4)+(p2/2)*sp.Rational(3,8)))
    assert sp.simplify(moment - p**2*p2/4)==0
    C = sp.simplify(-Fppp/Fp*a**2*(1-2*t)/(24*t*(1-t)))
    assert sp.simplify(C.subs(lam,0)-a**2*(1-2*t)/(48*t*(1-t)))==0
    assert sp.simplify(C.subs(lam,sp.Rational(1,3)))==0
    print('SYMBOLIC_COEFFICIENTS_OK', 'Fppp/Fp=',Fppp/Fp,'general=',C)


def numeric():
    cases = [(0.25,4,1,1,0), (0.75,4,1,1,0),
             (0.25,4,1,1,1), (0.25,4,2,0.7,0),
             (0.25,4,2,0.7,1), (0.5,4,2,0.7,0)]
    count=0
    for t,a,theta,eps,lam in cases:
        C = -(3*lam-1)/2*a*a*(1-2*t)/(24*t*(1-t))
        for rho in (.15,.22,.3):
            A,delta,dx,cube,T = orbit(rho,t,a,theta,eps,lam)
            assert abs(dx)<2e-9
            if t==0.5:
                assert abs(delta)<5e-10
            else:
                assert C*delta>0, (t,a,theta,eps,lam,rho,A,delta,C)
                assert abs(delta/A**4-C)<0.04*max(1,abs(C)), (A,delta/A**4,C)
            if lam==0 and t!=0.5:
                assert abs(cube/A**4-(1-2*t)/(4*t*(1-t)))<0.07
            print(f't={t} a={a} theta={theta} eps={eps} lam={lam} rho={rho} '
                  f'A={A:.9g} mean_n_minus_t={delta:.9g} '
                  f'ratio={delta/A**4:.8g} predicted={C:.8g} '
                  f'period={T:.8g}')
            count+=1
    print('PERIODIC_ORBIT_NUMERICS_OK cases=',count)


if __name__=='__main__':
    symbolic()
    numeric()
