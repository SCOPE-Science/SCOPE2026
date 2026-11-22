#!/usr/bin/env python3
"""Deterministic numerical diagnostics for near-circular Lame-boundary chord tails.

Requires NumPy and SciPy. Numerical diagnostics do not prove the limit theorem.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

LOG2 = math.log(2)


def entropy(theta):
    c=math.cos(theta)**2
    s=math.sin(theta)**2
    return -sum(u*math.log(u) if u>0 else 0.0 for u in (c,s))


def profile(lam, x=1.):
    if x<=0: return 0.
    if lam==0: return 2*math.sqrt(x)/math.pi
    if lam>0:
        if lam*LOG2/2<=x:
            lo=0.
        else:
            lo=brentq(lambda t: lam*(LOG2-entropy(t))/2-x,0.,math.pi/4)
        g=lambda t: (8/math.pi**2)*math.sqrt(max(0.,x-lam*(LOG2-entropy(t))/2))
        return quad(g, lo, math.pi/4,epsabs=2e-11,limit=200)[0]
    L=-lam
    if L*LOG2/2<=x:
        hi=math.pi/4
    else:
        hi=brentq(lambda t: L*entropy(t)/2-x,0.,math.pi/4)
    g=lambda t: (8/math.pi**2)*math.sqrt(max(0.,x-L*entropy(t)/2))
    return quad(g,0.,hi,epsabs=2e-11,limit=200)[0]


def radial(p, th):
    c=np.cos(th);s=np.sin(th)
    cp=np.abs(c)**p;sp=np.abs(s)**p
    ss=cp+sp
    return ss**(-1/p)


def arc_speed(p, th):
    c=np.cos(th);s=np.sin(th)
    cp=np.abs(c)**p;sp=np.abs(s)**p
    ss=cp+sp
    ds=-(np.abs(c)**(p-1))*np.sign(c)*s+(np.abs(s)**(p-1))*np.sign(s)*c
    r=ss**(-1/p)
    return r*np.sqrt(1+(ds/ss)**2)


def direct_probability(eps,lam,x=1., nalpha=1000,nbeta=1000):
    p=2+lam*eps
    assert p>1 and eps>0 and x>0
    D=2 if p<=2 else 2**(1.5-1/p)
    a=(np.arange(nalpha)+.5)*2*math.pi/nalpha
    da=2*math.pi/nalpha
    speed_a=arc_speed(p,a)
    P=float(speed_a.sum()*da)
    beta_max=3*math.sqrt(eps*x)
    b=(np.arange(nbeta)+.5)*(2*beta_max/nbeta)-beta_max
    db=2*beta_max/nbeta
    out=0.
    # loop over first endpoints, vectorize the second angular displacement
    for ai,si in zip(a,speed_a):
        r1=float(radial(p,ai))
        a2=ai+math.pi+b
        r2=radial(p,a2)
        chord=np.sqrt(r1*r1+r2*r2+2*r1*r2*np.cos(b))
        s2=arc_speed(p,a2)
        out+=si*np.sum(s2*(chord>=D-eps*x))*da*db
    return out/P**2


def main():
    n=0
    for lam in (-10.,-3.,0.,2.,10.):
        f=profile(lam)
        assert 0<f<=2/math.pi+1e-13
        print('profile',lam,format(f,'.12f'))
        n+=1
    for lam in (-4.,0.,4.):
        pred=profile(lam)
        for eps in (.0006,.00015):
            direct=direct_probability(eps,lam,nalpha=800,nbeta=900)/math.sqrt(eps)
            assert abs(direct/pred-1)<.035,(lam,eps,direct,pred)
            n+=1
    for lam in (30.,100.,1000.,10000.):
        value=profile(lam)
        leading=2/(math.pi*math.sqrt(lam))
        assert abs(value/leading-1)<.2,(lam,value,leading)
        n+=1
    for L in (1000.,10000.,100000.):
        value=profile(-L)
        leading=2*math.sqrt(2)/(math.pi*math.sqrt(L*math.log(L)))
        assert .65<value/leading<1.3,(L,value,leading)
        n+=1
    # Shannon binary entropy: zero at axial contacts and log(2) at diagonals.
    assert entropy(0.)==0.0
    assert abs(entropy(math.pi/4)-LOG2)<1e-14
    n+=2
    print('ALL_CHECKS_PASSED',n)

if __name__=='__main__': main()
