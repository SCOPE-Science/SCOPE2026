#!/usr/bin/env python3
"""Reproducible checks for polygon-calibrated piecewise-affine oscillators.

Requires Python, NumPy, SciPy and SymPy. These checks support, but do not
replace, the geometric proof for all admissible polygons.
"""
from math import exp
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq


def det(v, w):
    return float(np.linalg.det(np.stack((v, w), axis=1)))


def data(vertices, a, omega):
    P = np.array(vertices, dtype=float)
    assert len(P) == len(omega) and len(P) >= 3
    q = np.roll(P, -1, axis=0)
    E = q - P
    Delta = np.array([det(p, z) for p, z in zip(P, q)])
    assert np.all(Delta > 0)
    L2 = np.sum(E * E, axis=1)
    C = np.sum(P * E, axis=1) / L2
    W = np.array(omega, dtype=float)
    assert np.min(W) > a/2
    return P, E, Delta, L2, a/L2, a*(C+0.5)/Delta, W


def raw_vector(field, i, x):
    P, E, Delta, L2, lam, mu, omega = field
    e = E[i]
    n = np.array([e[1], -e[0]])
    V = np.dot(n, x) - Delta[i]
    return (omega[i] - mu[i]*V)*e - lam[i]*V*n


def point(field, i, r, u):
    P, E = field[:2]
    return r*(P[i]+u*E[i])


def ray_exit_time(r, u, omega, a):
    s = r-1
    def f(t):
        return omega*t - (1-r*u) - 0.5*s*(1+exp(-a*t))
    assert f(0) <= 1e-13
    upper = max(5.0, 4.0*(1+r)/omega)
    assert f(upper) > 0
    return brentq(f, 0.0, upper, xtol=1e-13)


def exact_point(field, i, r, u, t, a):
    s = r-1
    rt = 1+s*exp(-a*t)
    b = r*u+field[-1][i]*t-0.5*s*(1-exp(-a*t))
    P, E = field[:2]
    return rt*P[i]+b*E[i], rt, b/rt


def symbolic_check():
    p, q, dx, dy, a, omega, r, u = sp.symbols(
        'p q dx dy a omega r u', real=True)
    P = sp.Matrix([p,q]); E = sp.Matrix([dx,dy]); n = sp.Matrix([dy,-dx]);
    D = p*dy-q*dx
    L2 = dx**2+dy**2
    c = (P.dot(E))/L2
    lam = a/L2
    mu = a*(c+sp.Rational(1,2))/D
    X = r*(P+u*E)
    V = (n.dot(X)-D).cancel()
    F = (omega-mu*V)*E-lam*V*n
    rad = -a*(r-1)
    axial = omega - sp.Rational(1,2)*a*(r-1)
    F_expected = rad*P+axial*E
    assert sp.simplify(V - D*(r-1)) == 0
    assert all(sp.simplify(z) == 0 for z in (F-F_expected))
    du = (axial-u*rad)/r
    assert sp.simplify(du-(omega+a*(u-sp.Rational(1,2))*(r-1))/r) == 0


def geometric_check():
    polygons = [
        [(2,0), (1,2), (-1,2), (-2,-1), (0,-2)],
        [(3,0), (.5,1.4), (-1,2.2), (-1.8,-1), (.2,-3)],
    ]
    a = 0.8; omega = [1.1,1.3,.9,1.7,1.2]
    fields = [data(p,a,omega) for p in polygons]
    R = 1+2*min(omega)/a
    local_checks = 0
    full_cycle_checks = 0
    for field in fields:
        for r0 in [0.05, 0.25, 0.65, 0.999, 1, 1.3, 2.1, R-.01]:
            for u0 in [0, .17, .67, .99]:
                for i in range(len(omega)):
                    exit_time = ray_exit_time(r0,u0,omega[i],a)
                    assert exit_time >= 0
                    x0 = point(field,i,r0,u0)
                    sol = solve_ivp(lambda t,x:raw_vector(field,i,x),
                                    [0,exit_time],x0,rtol=2e-12,atol=2e-13,
                                    dense_output=True)
                    assert sol.success
                    for fraction in [.07, .29, .66, 1.]:
                        tt = exit_time*fraction
                        x_pred, r_pred, u_pred = exact_point(field,i,r0,u0,tt,a)
                        assert np.linalg.norm(sol.sol(tt)-x_pred) < 2e-8, (i,r0,u0,tt)
                        assert abs(r_pred - (1+(r0-1)*exp(-a*tt))) < 1e-13
                        assert -1e-12 <= u_pred <= 1+1e-12
                        local_checks += 1
        for r0 in [0.05, .8, 1, 2.5, R-0.001]:
            phase = 0.
            r = r0
            for i in range(len(omega)):
                tau = ray_exit_time(r,0,omega[i],a)
                phase += tau
                r = 1+(r-1)*exp(-a*tau)
                full_cycle_checks += 1
            assert abs(r-(1+(r0-1)*exp(-a*phase))) < 3e-12
    # The first-hit time and entire sequence of radial values must be shape invariant.
    for r0 in [0.1,1.,2.6,R-0.0001]:
        for i in range(5):
            for u0 in [0,.37,.89]:
                times = [ray_exit_time(r0,u0,field[-1][i],a) for field in fields]
                assert abs(times[0]-times[1]) < 1e-12
    return local_checks, full_cycle_checks, R


if __name__ == '__main__':
    symbolic_check()
    n, cycles, R = geometric_check()
    print('VERIFY_OK symbolic_vector_identity=True local_ode_checks=%d '
          'full_cycle_step_checks=%d polygon_shapes=2 forward_radius=%.12g '
          'shape_invariant_event_times=True' % (n,cycles,R))
