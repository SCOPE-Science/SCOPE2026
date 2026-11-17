#!/usr/bin/env python3
"""Numerical diagnostics for maximum-area triangle orientation on ellipse boundaries.
This script checks finite-threshold data against independently integrated limiting coefficients.
Numerical diagnostics are not proofs of asymptotic statements.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import ellipe

def predicted(q):
    assert 0 <= q < 1
    f=lambda t: math.sqrt(1 - q*math.cos(2*t))
    I=quad(f,0,2*math.pi,epsabs=2e-12)[0]
    D=lambda t: 1-.75*q*q-.25*q**3*math.cos(6*t)
    J=quad(lambda t:math.sqrt(D(t)),0,2*math.pi,epsabs=2e-12)[0]
    M=quad(lambda t:math.cos(6*t)*math.sqrt(D(t)),0,2*math.pi,epsabs=2e-12)[0]/J
    K=16*math.pi/3*J/I**3
    return K,M

def test_sim(q,n=2_000_000,t=0.035,seed=20261110):
    b=math.sqrt((1-q)/(1+q))
    rng=np.random.default_rng(seed)
    angles=[]
    while sum(z.size for z in angles)<3*n:
        x=rng.uniform(0,2*math.pi,4*n)
        y=rng.uniform(0,1,4*n)
        select=x[y < np.sqrt(np.sin(x)**2+b*b*np.cos(x)**2)]
        angles.append(select)
    ang=np.concatenate(angles)[:3*n].reshape(-1,3)
    # normalized area of ellipse-affine triangle
    area=np.abs(np.sin(ang[:,1]-ang[:,0])+np.sin(ang[:,2]-ang[:,1])+np.sin(ang[:,0]-ang[:,2]))/2
    event=(3*math.sqrt(3)/4-area<t)
    p=event.mean()
    m=np.cos(6*ang[event,0]).mean()
    K,M=predicted(q)
    std=math.sqrt(p*(1-p)/n)/t
    err_m=math.sqrt(np.var(np.cos(6*ang[event,0]))/max(1,event.sum()))
    print(f'q={q:.2f} n={n} eps={t} events={event.sum()} empirical_K={p/t:.7f} limit_K={K:.7f} MC_se_K={std:.7f} empirical_M6={m:.7f} limit_M6={M:.7f} MC_se_M6={err_m:.7f}')
    assert abs(p/t-K)<.12*K+5*std
    assert abs(m-M)<.10+5*err_m

if __name__=='__main__':
    for q in [0,.35,.70,.92]:
        print('quadrature q, K, M6:',q,*predicted(q))
        test_sim(q,n=550_000,t=.025,seed=20261110+int(q*100))
    k0,m0=predicted(0)
    assert abs(k0-4/(3*math.pi))<1e-12 and abs(m0)<1e-12
    # The limiting flat-ellipse values are established analytically.
    qs=[.10,.25,.45,.65,.85,.97,.995]
    ms=[predicted(q)[1] for q in qs]
    assert all(0>ms[i]>ms[i+1] for i in range(len(ms)-1))
    print('ELLIPSE_MAX_TRIANGLE_SIXTH_HARMONIC_CHECK_OK')
