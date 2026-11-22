#!/usr/bin/env python3
"""Deterministic numerical diagnostics for the spherical-cap shadow-area theorem.
This is not a computer-assisted proof or an exhaustive certification.
"""
import math

PI = math.pi

def projected_area(h, c):
    assert -1.0 < h < 1.0 and 0.0 <= c <= 1.0
    r = math.sqrt(1-h*h)
    s = math.sqrt(max(0.0, 1-c*c))
    if h > 0 and s <= h:
        return PI*r*r*c
    if h < 0 and s <= -h:
        return PI
    if s == 0:  # hemisphere at the axial endpoint
        return PI
    beta = math.acos(max(-1.0, min(1.0, -h*c/(r*s))))
    return math.acos(max(-1.0, min(1.0, h/s))) + r*r*c*beta - h*r*s*math.sin(beta)

def latitude_integral(h, c, n=4000):
    """Independent 1D quadrature: integrate positive part over longitude analytically."""
    s = math.sqrt(max(0.0, 1-c*c))
    def integrand(t):
        a = c*t
        b = s*math.sqrt(max(0., 1-t*t))
        if b < 1e-15:
            return 2*PI*max(a, 0.)
        if a >= b:
            return 2*PI*a
        if a <= -b:
            return 0.
        beta = math.acos(-a/b)
        return 2*(a*beta + b*math.sin(beta))
    dt = (1.-h)/n
    acc = integrand(h) + integrand(1.)
    for i in range(1,n):
        acc += (4 if i%2 else 2)*integrand(h+i*dt)
    return acc*dt/3.

def run():
    nchecks=0
    for h in (-.9,-.6,-.3,-.03,0.,.04,.2,.5,.9):
        r=math.sqrt(1-h*h)
        bmin=math.acos(h)-h*r
        cs=[j/20 for j in range(21)]
        ps=[projected_area(h,c) for c in cs]
        assert abs(ps[0]-bmin)<2e-12; nchecks+=1
        assert all(x <= y+1e-10 for x,y in zip(ps,ps[1:])); nchecks+=1
        for c,p in zip(cs,ps):
            q=latitude_integral(h,c)
            assert abs(p-q)<2e-5, (h,c,p,q)
            nchecks+=1
        for c in (.123,.377,.821):
            if h<0 and c>=r:
                assert abs(projected_area(h,c)-PI)<1e-12
            elif h>0 and c>=r:
                assert abs(projected_area(h,c)-PI*r*r*c)<1e-12
            nchecks+=1
    for h in (-.7,-.25,.25,.65):
        a=abs(h);r=math.sqrt(1-h*h)
        d=0.0008;s=a+d;c=math.sqrt(1-s*s)
        b=projected_area(h,c)
        base=PI*r*r*c if h>0 else PI
        coef=8*math.sqrt(2)/(15*r*r*math.sqrt(a))
        ratio=(b-base)/(d**2.5)
        assert abs(ratio-math.copysign(coef,h))/coef < 0.015, (h,ratio,coef)
        nchecks+=1
    # The atomic-tail local coefficient is checked independently in c, not in s.
    for h in (-.7,-.4,-.2):
        a=-h;r=math.sqrt(1-h*h);dc=.0003
        K=8*math.sqrt(2)*math.sqrt(r)/(15*a**3)
        deficit=PI-projected_area(h,r-dc)
        assert abs(deficit/dc**2.5-K)/K < .06
        nchecks+=1
    print('PASS:', nchecks, 'deterministic diagnostic assertions')

if __name__=='__main__':
    run()
