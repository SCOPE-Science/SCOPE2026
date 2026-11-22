#!/usr/bin/env python3
"""Numerical independent tests of two equal-covariance random-diffusivity models.

Requires numpy and scipy. Both moment hierarchies are derived from their
respective infinitesimal generators, not from the integrated-cumulant formula.
"""
import math
import numpy as np
from scipy.linalg import expm

COUNT = 0

def check(x, y, rtol=2e-8, atol=2e-8, label=''):
    global COUNT
    COUNT += 1
    if not np.isclose(x, y, rtol=rtol, atol=atol):
        raise AssertionError(f'{label}: {x} versus {y}')

def odd_df(j):
    a = 1
    for k in range(1, j+1):
        a *= 2*k-1
    return a

def ou_integrated_moments(t, m, q, N=4):
    """Generator hierarchy for E[A^n Y^(2j)], n+j<=N."""
    inds = [(n,j) for n in range(N+1) for j in range(N+1-n)]
    idx = {v:i for i,v in enumerate(inds)}
    H = np.zeros((len(inds),len(inds)))
    initial = np.zeros(len(inds))
    for i,(n,j) in enumerate(inds):
        if n == 0:
            initial[i] = odd_df(j)*m**j
        H[i,i] = -q*j
        if n > 0:
            H[i,idx[(n-1,j+1)]] += n
        if j > 0:
            H[i,idx[(n,j-1)]] += q*m*j*(2*j-1)
    result = expm(H*t) @ initial
    return [result[idx[(n,0)]] for n in range(N+1)]

def binary_integrated_moments(t, m, q, u, N=4):
    """Occupation-weighted generator hierarchy for E[A^n 1_{S=i}]."""
    p = u*u/(u*u+2)
    low,high = m*(1-u), m*(1+2/u)
    Q = np.array([[-q*p,q*p],[q*(1-p),-q*(1-p)]])
    H = np.zeros((2*(N+1),2*(N+1)))
    for n in range(N+1):
        H[2*n:2*n+2,2*n:2*n+2] += Q.T
        if n:
            H[2*n:2*n+2,2*n-2:2*n] += n*np.diag([low,high])
    initial = np.zeros(2*(N+1))
    initial[:2] = (1-p,p)
    result = expm(H*t) @ initial
    return [sum(result[2*n:2*n+2]) for n in range(N+1)]

def cumulants_X(A):
    mu = [0]+[odd_df(n)*(2**n)*A[n] for n in range(1,5)]
    v,z,h,f=mu[1:]
    return [v, z-3*v*v,
            h-15*z*v+30*v**3,
            f-28*h*v-35*z*z+420*z*v*v-630*v**4]

def F(q,t):
    # Integrals avoid cancellation near t=0
    z = q*t
    return (z-1+math.exp(-z))/(q*q)

def J(q,t):
    z=q*t
    return (z-2+(z+2)*math.exp(-z))/(q**3)

def exact_cum(t,m,q,u):
    return (2*m*t,48*m*m*F(q,t),
            1440*m**3*(2/u-u)*J(q,t))

def exact_ou(t,m,q):
    return (2*m*t,48*m*m*F(q,t),5760*m**3*J(q,t))

uc=math.sqrt(6)-2
check(2/uc-uc,4,atol=1e-14, label='critical ratio')
# Identical one-, two- and three-point diffusivity moments at the crossover.
for m in (0.3,1.0,2.2):
    for q in (0.4,1.1,2.9):
        for t in (0.6,1.2,2.5):
            bg = cumulants_X(ou_integrated_moments(t,m,q))
            for i, expected in enumerate(exact_ou(t,m,q)):
                check(bg[i],expected,label=f'OU cumulant_{2*i+2}')
            for u in (0.16, 0.35, uc, 0.67, 0.92):
                bt=cumulants_X(binary_integrated_moments(t,m,q,u))
                for i,expected in enumerate(exact_cum(t,m,q,u)):
                    check(bt[i],expected,label=f'binary cumulant_{2*i+2}')
                check(bt[0],bg[0],label='same second')
                check(bt[1],bg[1],label='same fourth')
                if u == uc:
                    check(bt[2],bg[2],atol=1e-7,label='sixth crossing')
                    z0=q*t
                    h = 12*z0 + 24*z0*math.exp(-z0) - 30 + 24*math.exp(-z0) + 6*math.exp(-2*z0)
                    check(bg[3]-bt[3],40320*m**4*h/q**4,rtol=3e-7,atol=3e-7,label='eighth gap')
                    assert bg[3]>bt[3], ('eighth gap ordering',m,q,t)
                    COUNT+=1
                elif u<uc:
                    assert bt[2]>bg[2], ('wrong sixth ordering',u)
                    COUNT+=1
                else:
                    assert bt[2]<bg[2], ('wrong sixth ordering',u)
                    COUNT+=1
# Near-zero eighth cumulant difference should tend to 40320 m^4 t^4.
for t in (0.02,0.03,0.05):
    m,q=1.0,1.0
    kg=cumulants_X(ou_integrated_moments(t,m,q))[3]
    kt=cumulants_X(binary_integrated_moments(t,m,q,uc))[3]
    check((kg-kt)/t**4,40320,rtol=0.13,label='eighth asymptotic')
print(f'PASS {COUNT} generator-hierarchy and analytic assertions')
