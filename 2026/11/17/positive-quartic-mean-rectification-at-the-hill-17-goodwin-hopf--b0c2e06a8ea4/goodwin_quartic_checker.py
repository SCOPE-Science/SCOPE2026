#!/usr/bin/env python3
"""Exact rational and optional numerical checks for fourth-order Goodwin mean rectification."""
import argparse
import sympy as sp


def exact_checks():
    t = sp.symbols('t')
    m = 17
    r = sp.Rational(8, m - 8)
    h = (1 + r) / (1 + r*t**m)
    deriv = [sp.diff(h, t, j).subs(t, 1) for j in range(1, 5)]
    assert deriv == [-8, 0, 1152, -2304], deriv
    J = sp.Matrix([[-1, 0, -8], [1, -1, 0], [0, 1, -1]])
    omega = sp.sqrt(3)
    q = sp.Matrix([(1 + sp.I*omega)**2, 1 + sp.I*omega, 1])
    assert sp.simplify((J - sp.I*omega*sp.eye(3))*q) == sp.zeros(3, 1)
    # The conjugated first component of the normalized adjoint eigenvector.
    conjugate_p_first = (-1 - sp.I*omega)/24
    G = sp.simplify(conjugate_p_first * deriv[2])
    assert sp.simplify(sp.re(G) + 48) == 0
    l1 = sp.simplify(sp.re(G)/(2*omega))
    assert l1 == -8*omega
    # In units of the Hopf equilibrium level, detuning is 2a^2+O(a^4).
    shift2 = sp.simplify((deriv[2]/8)/72)
    assert shift2 == 2
    # Averaged (D+1)^3 equation gives 9*mean4 = 1152*shift2/4 - 2304/64.
    mean4 = sp.simplify((deriv[2]*shift2/4 + deriv[3]/64)/9)
    assert mean4 == 60
    print('GOODWIN_QUARTIC_EXACT_OK derivatives=4 l1=-8sqrt3 shift2=2 mean4=60')


def numeric_checks():
    import numpy as np
    from scipy.integrate import solve_ivp
    from scipy.optimize import brentq
    m=17
    e0=(8/9)**(1/17)
    K0=e0*(1+e0**m)
    for pct in [0.005, 0.01, 0.02]:
        K=K0*(1+pct)
        e=brentq(lambda v:v*(1+v**m)-K, .5, 1.5)
        def rhs(t,v):
            x,y,z,I=v
            return [K/(1+z**m)-x, x-y, y-z, z]
        def event(t,v):return v[2]-e
        event.direction=1
        sol=solve_ivp(rhs,[0,1900],[.98*e,.99*e,.99*e,0],events=event,
                      dense_output=True,method='DOP853',rtol=1e-11,atol=1e-13,max_step=1)
        crossings=sol.t_events[0]
        assert len(crossings)>25
        a,b=crossings[-21],crossings[-1]
        vals=sol.sol(np.linspace(a,b,8001))[2]
        amp=(np.max(vals)-np.min(vals))/2
        mean=(sol.sol(b)[3]-sol.sol(a)[3])/(b-a)
        predicted=60*amp**4/e0**3
        assert predicted>0 and abs((mean-e)/predicted-1)<.04,(pct,mean-e,predicted)
    print('GOODWIN_QUARTIC_NUMERIC_OK three_near_hopf_cases=3')


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--numeric',action='store_true')
    args=parser.parse_args()
    exact_checks()
    if args.numeric:numeric_checks()
