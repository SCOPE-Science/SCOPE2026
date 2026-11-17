#!/usr/bin/env python3
"""Finite numerical checks for one-step sketched Ritz laws (stdlib)."""
import math
import random

SEED=20261102
rng=random.Random(SEED)

def formula_angle(k):
    return 2*math.sqrt(k)/(k+1)

def pnegative_s1(rho):return math.acos(rho)/math.pi

def pnegative_s2(rho):return (1-rho)/2

def pnegative_s3(rho):
    sigma=math.sqrt(1-rho*rho)
    return (math.asin(sigma)-sigma*rho)/math.pi

def tail_constant(s,rho,alpha=1):
    return 2*alpha*math.exp(math.lgamma((s+1)/2)-math.lgamma(s/2)-math.log(math.pi)/2)*(1-rho*rho)**(s/2)

def formula_curvature(k):
    b=(math.sqrt(k/(k+1)), math.sqrt(1/(k+1)))
    Ab=(b[0], k*b[1])
    alpha=math.hypot(*Ab)
    rho=(b[0]*Ab[0]+b[1]*Ab[1])/alpha
    return b,Ab,alpha,rho

# Check exact spectral extremal and minimization on grids.
for k in (1.001,1.1,2.0,4.0,16.0,100.0):
    b,Ab,alpha,rho=formula_curvature(k)
    assert abs(rho-formula_angle(k))<2e-14,(k,rho)
    for q in range(1001):
        p=q/1000
        x=(math.sqrt(1-p),math.sqrt(p))
        Ax=(x[0], k*x[1]); dot=x[0]*Ax[0]+x[1]*Ax[1]
        rr=dot/math.hypot(*Ax)
        assert rr>rho-2e-13,(k,p,rr,rho)

# Matrix implementation matches correlation law in 2D at multiple sketch sizes.
for k,s,trials in ((4,1,40000),(4,2,40000),(4,3,40000),(16,2,40000),(9,3,40000)):
    b,Ab,alpha,rho=formula_curvature(k)
    cnt=0
    for j in range(trials):
        sx=sy=vv=0.0
        for _ in range(s):
            g0,g1=rng.gauss(0,1),rng.gauss(0,1)
            u=g0*b[0]+g1*b[1]
            v=g0*Ab[0]+g1*Ab[1]
            sx+=u*u;sy+=u*v;vv+=v*v
        cnt+=sy<0
        harn=sy/sx
        hhm=vv/sy
        assert (harn<0)==(hhm<0)
        assert abs(harn*hhm-vv/sx)<1e-9*max(1,vv/sx)
    estimate=cnt/trials
    target={1:pnegative_s1,2:pnegative_s2,3:pnegative_s3}[s](rho)
    assert abs(estimate-target)<0.017,(s,k,estimate,target)
    print(f's={s}, condition={k:g}, empirical_negative={estimate:.6f}, exact={target:.6f}')

# Analytic tail constant from reciprocal shifted t distribution, evaluated independently
# at the Student-t density x=0 and compared to the stated gamma formula.
for s in range(1,18):
    for rho in (0.01,0.2,0.6,0.99):
        sigma=math.sqrt(1-rho*rho)
        logf=math.lgamma((s+1)/2)-math.lgamma(s/2)-0.5*math.log(math.pi)-math.log(sigma)+ (s+1)*math.log(sigma)
        assert math.isclose(2*math.exp(logf),tail_constant(s,rho),rel_tol=2e-14)

print('VERIFY_OK')
