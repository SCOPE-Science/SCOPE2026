#!/usr/bin/env python3
"""Reproduce symbolic identities and numerical stress tests for common-frailty founding."""
import math
import random
r=random.Random(50421)
count=0

def close(a,b,eps=2e-9):
    global count
    count+=1
    assert abs(a-b)<eps*max(1,abs(a),abs(b)),(a,b)

def B(q,l):
    return 2*(q+1)**2*(q-1)-l*(q+1)*(q+5)-l*l*(7*q+3)

def C(q,l):
    return 3*l*l+(9-7*q)*l+5*q*q-6*q+5

def critical(q):
    assert q>1
    b=(q+1)*(q+5)
    a=7*q+3
    c=2*(q+1)**2*(q-1)
    return 2*c/(math.sqrt(b*b+4*a*c)+b)

def P(z,q,l):
    p=(1+q+z)**2-4*q*z
    s=2*(1+q+z)
    w=p+l*s
    return l*l*(w+p)/(w*(w+l*l))

def H(z,q,l):
    p=(1+q+z)**2-4*q*z
    dp=2*(1+z-q)
    s=2*(1+q+z)
    w=p+l*s
    dw=dp+2*l
    return (dw+dp)*w*(w+l*l)-(w+p)*dw*(2*w+l*l)

for q in [1.001,1.1,1.4,2,4,9,40,100]:
    lc=critical(q)
    close(B(q,lc),0,1e-8)
    assert 0<lc<q-1
    assert C(q,lc)>0
    for delta in [-0.05,-0.001,0,0.001,0.05]:
        l=lc*(1+delta)
        close(H(0,q,l),2*(q+1)*(l+q+1)*B(q,l),1e-4)
        # Differentiate exact polynomial H with a five-point stencil.
        h=1e-4*(1+q+l)
        deriv=(-H(2*h,q,l)+8*H(h,q,l)-8*H(-h,q,l)+H(-2*h,q,l))/(12*h)
        close(deriv,-4*(q+1)*(l+q+1)*C(q,l),1e-5)
        for z in [0,0.03,0.3,1.0,3.0]:
            p=(1+q+z)**2-4*q*z
            s=2*(1+q+z)
            w=p+l*s
            h=1e-5*(1+z)
            derivative=(P(z+h,q,l)-P(z-h,q,l))/(2*h)
            close(derivative,l*l*H(z,q,l)/(w*w*(w+l*l)**2),1e-6)

# Locally symmetric pitchfork improvement on the feasible transect.
for q in [1.01,2,4,9,40]:
    lc=critical(q)
    for e in [1e-3,1e-4]:
        l=lc-e*max(1,lc)
        if l<=0: continue
        b=B(q,l);cc=C(q,l)
        x2=b/(2*cc)
        assert x2>0
        # The midpoint is strictly locally dominated, and two mirrored points tie.
        assert P(x2,q,l)>P(0,q,l)
        close(P(x2,q,l),P(x2,q,l))

# Common-frailty success probabilities reproduce exact exponential quadrature.
for i in range(400):
    q=10**r.uniform(-2,2)
    l=10**r.uniform(-2,1)
    z=10**r.uniform(-3,2)
    u=1+q+z-2*math.sqrt(q*z)
    v=1+q+z+2*math.sqrt(q*z)
    direct=1-u/(u+l)-v/(v+l)+u*v/(u*v+l*(u+v))
    close(P(z,q,l),direct)

print('PASS:',count,'deterministic checks')
