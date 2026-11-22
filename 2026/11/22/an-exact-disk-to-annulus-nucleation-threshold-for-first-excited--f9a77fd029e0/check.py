"""Finite diagnostics for the first excited-wavelet fixed-state mask theorem.

Requires Python 3, scipy, and numpy.  These tests supplement, not replace,
the analytic derivation and the bathtub comparison proof.
"""
import math
import mpmath as mp
from scipy.optimize import brentq
from scipy.integrate import quad

PI = math.pi

def ingredients(a):
    assert a > 0
    u0 = 1.0 / (a+2.0)
    up = (3*a+5)/((a+2)*(a+3))
    f = lambda u: (1.0-u)**(a+1.0)*(1.0-(a+2.0)*u)**2
    cp = f(up)
    xstar = brentq(lambda x: f(x)-cp, 0.0, u0)
    hstar = 4*PI*xstar/(1-xstar)
    F = lambda u: 1.0-(1.0-u)**a*(1.0+a*(a+2.0)*u*u)
    return u0,up,f,cp,xstar,hstar,F

def endpoints(a, threshold):
    u0,up,f,cp,xstar,hstar,F = ingredients(a)
    if threshold>=cp:
        x=brentq(lambda u:f(u)-threshold,0,u0)
        return ((0.,x),)
    x=brentq(lambda u:f(u)-threshold,0,u0)
    lo=brentq(lambda u:f(u)-threshold,u0,up)
    hi=brentq(lambda u:f(u)-threshold,up,1-1e-12)
    return ((0.,x),(lo,hi))

def area(intervals):
    return 4*PI*sum(b/(1-b)-a/(1-a) for a,b in intervals)

def captured(a, intervals):
    F=ingredients(a)[-1]
    return sum(F(b)-F(z) for z,b in intervals)

counter=0
for a in (0.2,1.0,2.5,10.0):
    u0,up,f,cp,xstar,hstar,F=ingredients(a)
    assert 0<xstar<u0<up<1 and 0<cp<1
    assert abs(F(1.0)-1)<1e-12
    assert abs(quad(lambda u:a*(1-u)**(a-1)*(1-(a+2)*u)**2,0,1)[0]-1)<1e-10
    counter+=3
    for ratio in (.25,.75,1.0,1.25,2.0,4.0):
        h=ratio*hstar
        if ratio==1:
            c=cp
        else:
            c=brentq(lambda v:area(endpoints(a,v))-h, 1e-8, 1-1e-9)
        ints=endpoints(a,c)
        assert len(ints)==(1 if ratio<=1 else 2)
        assert abs(area(ints)-h)<1e-5
        direct=sum(quad(lambda u: a*(1-u)**(a-1)*(1-(a+2)*u)**2, lo, hi,epsabs=1e-11)[0] for lo,hi in ints)
        assert abs(direct-captured(a,ints))<1e-10
        counter+=3
    # High-precision near-birth calculations: the level gap is quadratic in area.
    mp.mp.dps=60
    aa=mp.mpf(str(a)); cc=aa+2
    pup=(3*aa+5)/(cc*(aa+3)); zero=1/cc
    fm=lambda u:(1-u)**(aa+1)*(1-cc*u)**2
    pcrit=fm(pup)
    star=mp.findroot(lambda u:fm(u)-pcrit,(mp.mpf(0),zero*mp.mpf('0.99')))
    hs=4*mp.pi*star/(1-star)
    k=2*(aa+1)*cc*(1-pup)**aa
    slope=abs(cc*(aa+3)*(1-star)**aa*(1-cc*star)*(star-pup))
    for reltext in ('0.002','0.0002'):
        dh=mp.mpf(reltext)
        # Solve H as a function of the outer-ring half-width parameter.
        def values(w):
            lev=fm(pup+w)
            xin=mp.findroot(lambda u:fm(u)-lev,(star,star+mp.mpf('0.01')/cc))
            lo=mp.findroot(lambda u:fm(u)-lev,(pup-w*mp.mpf('1.2'),pup-w*mp.mpf('.8')))
            ar=4*mp.pi*(xin/(1-xin)+(pup+w)/(1-pup-w)-lo/(1-lo))
            return ar,xin,lo
        first=(1-pup)**2*dh/(8*mp.pi)
        w=mp.findroot(lambda t:values(t)[0]-(hs+dh),(first*mp.mpf('.8'),first*mp.mpf('1.2')))
        ar,xin,lo=values(w)
        width=(pup+w)-lo
        predicted_width=(1-pup)**2/(4*mp.pi)*dh
        predicted_shift=k*(1-pup)**4/(128*mp.pi**2*slope)*dh**2
        assert abs(width/predicted_width-1)<mp.mpf('.03')
        assert abs((xin-star)/predicted_shift-1)<mp.mpf('.03')
        counter+=2
# Exact alpha-one special case
u0,up,f,cp,xstar,hstar,F=ingredients(1.0)
assert abs(cp-1/9)<1e-12
assert abs(xstar-(2-math.sqrt(2))/3)<1e-12
assert abs(hstar-4*PI*(3*math.sqrt(2)-4))<1e-11
assert abs(F(xstar)-(8-5*math.sqrt(2))/9)<1e-12
counter+=4
print('PASS:',counter,'finite assertions across four wavelet parameters, budget regimes, near-threshold asymptotics, and the exact weight-one case')
