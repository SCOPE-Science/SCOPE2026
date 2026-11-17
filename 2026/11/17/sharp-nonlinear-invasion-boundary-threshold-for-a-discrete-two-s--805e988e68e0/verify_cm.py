#!/usr/bin/env python3
"""Finite algebraic checks for the quadratic reduction of a two-stage contagion map.
Python 3 standard library only. Does not establish infinite-time convergence.
"""
import math

def parameters(nu, tau, p):
    assert nu > 0 and tau > 0 and 0 < p <= 1
    m = nu * tau
    d = math.exp(-m)
    h = -math.expm1(-m)
    k = -math.expm1(-(1 + nu) * tau)
    H = 1 - (1 + m) * d
    rho = (1 + nu) * m / (p * h)
    C = rho * k / (1 + nu)
    q1 = C * h / m
    q2 = -C * C * H / (m * m)
    A = (1 - p) * q1 / h
    R = k / ((1 + nu) * h)
    psi = (1 - p)**2 - p * H / h - p*p*(h/k + 1/(1+nu))
    coeff_direct = p * q2 + q1 * ((1-p) * A - p*(1+R))
    coeff_closed = k*k*psi/(p*p*h)
    assert math.isclose(q1, k/p, rel_tol=1e-12)
    assert math.isclose(coeff_direct, coeff_closed, rel_tol=1e-11, abs_tol=1e-12)
    return m, d, k, C, A, R, coeff_closed, psi

def mapstep(v, a, r, nu, tau, p):
    m, d, k, C, A, R, c2, psi = parameters(nu,tau,p)
    q = C*a/(C*a+m)*(-math.expm1(-(C*a+m)))
    s0 = 1-v-a-r
    return ((1-p)*q*s0 + d*math.exp(-C*a)*v,
            p*q*s0 + q*v + (1-k)*a,
            d*r + k*a/(1+nu))

for nu,tau,p in [(0.1,1.0,0.25), (0.1,1.0,0.75), (0.002,5.5,0.75), (1.0,1.0,0.85), (0.1,1.0,1.0)]:
    m,d,k,C,A,R,c2,psi=parameters(nu,tau,p)
    for eps in [1e-4, 1e-5, 1e-6]:
        _, after, _ = mapstep(A*eps,eps,R*eps,nu,tau,p)
        approx=(after-eps)/(eps*eps)
        assert math.isclose(approx,c2, rel_tol=0.008,abs_tol=0.008),(nu,tau,p,approx,c2)
    H=1-(1+m)*d
    h=1-d
    L=h/k+1/(1+nu)
    J=H/h
    def psi_fn(t): return (1-t)**2-J*t-L*t*t
    lo,hi=0.0,1.0
    for _ in range(80):
        mid=(lo+hi)*0.5
        if psi_fn(mid)>0: lo=mid
        else: hi=mid
    pstar=(lo+hi)*0.5
    assert 0<pstar<1 and abs(psi_fn(pstar))<1e-12
print('VERIFY_OK quadratic_coefficients=5 direct_map_finite_differences=15 unique_threshold_bisections=5')
print('FINITE_CHECK_ONLY: exact local dynamics and infinite-time limits are analytical')
