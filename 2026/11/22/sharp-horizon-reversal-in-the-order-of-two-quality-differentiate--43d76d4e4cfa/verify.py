#!/usr/bin/env python3
"""Independent arithmetic checks for the two-pulse biomass/quality model.

Only the two impulse-ODE definitions and direct integration are needed.
These tests corroborate; the analytic identity and inequalities are the proof.
"""
import math
import random


def model_value(a,b,d,H,m,q0,q1):
    """Piecewise exact integration, for quality q0 at 0 and q1 at d."""
    c=a+b
    # For time 0..d: B = m exp(-at), Q = m q0 exp(-bt)
    pre=m*m*q0*(-math.expm1(-c*d))/c
    # For time d..H write s=t-d; B=m(e^-ad+1)e^-as,
    # Q=m(q0 e^-bd+q1)e^-bs.
    post=m*m*(1+math.exp(-a*d))*(q0*math.exp(-b*d)+q1)*(-math.expm1(-c*(H-d)))/c
    return pre+post


def contrast(a,b,d,H,m,qhi,qlo):
    c=a+b
    D=math.exp(-a*d)-math.exp(-b*d)
    E=-math.expm1(-c*d)
    z=math.exp(-c*(H-d))
    return m*m*(qhi-qlo)*((E+D)*z-D)/c


def threshold(a,b,d):
    assert 0<a<b and d>0
    D=math.exp(-a*d)-math.exp(-b*d)
    E=-math.expm1(-(a+b)*d)
    return d + math.log1p(E/D)/(a+b)


def model_quadrature(a,b,d,H,m,q0,q1,steps=300):
    # split at impulse time, composite midpoint quadrature
    def f(t):
        if t<d:
            return m*m*q0*math.exp(-(a+b)*t)
        B=m*(math.exp(-a*t)+math.exp(-a*(t-d)))
        Q=m*(q0*math.exp(-b*t)+q1*math.exp(-b*(t-d)))
        return B*Q
    s=0.0
    for lo,hi in [(0.,d),(d,H)]:
        if hi<=lo: continue
        dt=(hi-lo)/steps
        s+=dt*sum(f(lo+(i+.5)*dt) for i in range(steps))
    return s


def run():
    rng=random.Random(549321)
    count=0
    # Deterministic parameter test demonstrates reversal and exact threshold.
    a,b,d,m,qhi,qlo=1.,2.,1.,1.,.8,.2
    Hc=threshold(a,b,d)
    assert abs(Hc-1.5421744583454817)<2e-15
    count+=1
    for H in [d,1.1,1.3,Hc,1.8,2,3,6]:
        v0=model_value(a,b,d,H,m,qhi,qlo)
        v1=model_value(a,b,d,H,m,qlo,qhi)
        gap=contrast(a,b,d,H,m,qhi,qlo)
        assert abs((v0-v1)-gap)<3e-14
        count+=1
    for _ in range(6500):
        a=10**rng.uniform(-.7,.6)
        b=10**rng.uniform(-.7,.6)
        d=rng.uniform(.04,2.)
        H=d+rng.uniform(.0001,3.0)
        m=rng.uniform(.1,4.)
        qlo=rng.uniform(.001,.6)
        qhi=rng.uniform(qlo+.001,1.5)
        v0=model_value(a,b,d,H,m,qhi,qlo)
        v1=model_value(a,b,d,H,m,qlo,qhi)
        diff=contrast(a,b,d,H,m,qhi,qlo)
        assert abs(v0-v1-diff)<4e-12*max(1,v0,v1)
        count+=1
        if a>=b:
            assert diff>0
            count+=1
        else:
            hc=threshold(a,b,d)
            assert hc>d
            assert contrast(a,b,d,hc,m,qhi,qlo)==0 or abs(contrast(a,b,d,hc,m,qhi,qlo))<1e-13
            assert contrast(a,b,d,(d+hc)/2,m,qhi,qlo)>0
            assert contrast(a,b,d,hc+2,m,qhi,qlo)<0
            count+=4
    # An independent numerical integration method, avoiding the closed contrast.
    for _ in range(180):
        a,b=rng.uniform(.3,2),rng.uniform(.3,2)
        d=rng.uniform(.2,1)
        H=d+rng.uniform(.2,2)
        m=rng.uniform(.5,2)
        q0,q1=rng.uniform(.2,1),rng.uniform(.2,1)
        exact=model_value(a,b,d,H,m,q0,q1)
        numeric=model_quadrature(a,b,d,H,m,q0,q1,steps=700)
        assert abs(exact-numeric)<5e-6*max(1,exact)
        count+=1
    # Singular gap asymptotic: the switch can remain at positive horizon
    # as gap tends to zero, even though the flux difference vanishes.
    for a,b in [(.2,1.),(1.,2.),(.9,1.),(1.,4.)]:
        limiting=math.log(2*b/(b-a))/(a+b)
        for d in [.001,.0001,.00001]:
            assert abs(threshold(a,b,d)-limiting)<0.004
            count+=1
    return count

if __name__=='__main__':
    print('ASSERTIONS_PASSED',run())
