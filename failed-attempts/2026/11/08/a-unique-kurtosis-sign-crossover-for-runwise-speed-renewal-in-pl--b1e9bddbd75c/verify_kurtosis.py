#!/usr/bin/env python3
"""Independent deterministic checks for a Poisson-renewed planar velocity model.

This code uses only the mathematical model and its moment equations. It does not
claim to prove the infinite-time or all-parameter assertions on its own.
"""
import math
from scipy.integrate import quad, solve_ivp


def ij(s):
    # Independent positive-integral evaluation, stable for small s.
    i, _ = quad(lambda u: (s-u)*math.exp(-u)*u*u/2, 0, s,
                epsabs=3e-14, epsrel=3e-13)
    j, _ = quad(lambda u: (s-u)*math.exp(-u)*
                quad(lambda w: (u-w)*math.exp(-w), 0, u,
                     epsabs=3e-14)[0], 0, s, epsabs=3e-14)
    return i, j


def moments_ode(t, alpha, m2, m4):
    # D=0, x-component moments. y=(E[xu], E[x^2], E[xu^3],
    # E[x^2u^2], E[x^3u], E[x^4]).
    def rhs(_, y):
        a, var, c, b, p, f4 = y
        return [m2-alpha*a, 2*a,
                m4-alpha*c, 2*c-alpha*b+alpha*m2*var,
                3*b-alpha*p, 4*p]
    sol = solve_ivp(rhs, (0, t), [0]*6, method='DOP853', rtol=1e-12,
                    atol=1e-13)
    assert sol.success
    return sol.y[1, -1], sol.y[-1, -1]


def check():
    count = 0
    # Each speed law is R=1 with prob p and 0 otherwise: m2=p/2,
    # m4=3p/8. Include the critical boundaries p=1/2 and 3/4.
    for alpha in (0.4, 1.0, 2.7):
        for p in (0.3, 0.5, 0.6, 2/3, 0.75, 0.9, 1.0):
            m2, m4 = p/2, 3*p/8
            for s in (0.13, 0.7, 1.2, 2.9, 5.7, 12):
                t = s/alpha
                i, j = ij(s)
                cum = 24/alpha**4*((m4-m2*m2)*i - 2*m2*m2*j)
                var_exact = 2*m2*(t/alpha-(1-math.exp(-s))/alpha**2)
                var_ode, fourth_ode = moments_ode(t,alpha,m2,m4)
                cum_ode = fourth_ode - 3*var_ode**2
                assert math.isclose(var_exact, var_ode, rel_tol=5e-9,
                                    abs_tol=5e-11), (alpha,p,s,var_exact,var_ode)
                assert math.isclose(cum,cum_ode,rel_tol=2e-7,
                                    abs_tol=2e-10), (alpha,p,s,cum,cum_ode)
                rho=1/p
                threshold=2/3*(1+2*j/i)
                assert (cum>0)==(rho>threshold) or abs(cum)<1e-10
                count+=3
    # Check strict decrease and limiting endpoints numerically.
    ss=(0.01,0.04,0.15,0.5,1,2,4,8,16,40,100)
    thr=[2/3*(1+2*ij(s)[1]/ij(s)[0]) for s in ss]
    assert all(a>b for a,b in zip(thr,thr[1:])),thr
    assert 4/3<thr[-1]<thr[0]<2
    count+=len(ss)
    # For p=2/3 a sign change occurs near s=4, not merely a
    # monotone magnitude change.
    threshold_for=1/(2/3)
    signs=[]
    for s in (0.1,1,2,4,8,16):
        i,j=ij(s)
        signs.append(threshold_for>2/3*(1+2*j/i))
    assert signs == [False,False,False,True,True,True],signs
    count+=len(signs)
    print(f'PASS: {count} deterministic checks, including 252 independent ODE/moment comparisons')

if __name__ == '__main__':
    check()
