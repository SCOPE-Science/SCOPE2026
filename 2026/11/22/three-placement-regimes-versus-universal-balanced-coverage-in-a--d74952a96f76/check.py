#!/usr/bin/env python3
"""Numerical reproducibility checks for the two-site distance-decay service theorem."""
import math
import random

def intensity(x, d, strength):
    return strength * math.exp(-abs(x-d))

def mean_served(x, d, strength):
    return 2-math.exp(-intensity(x,d,strength))-math.exp(-intensity(x,-d,strength))

def both_served(x, d, strength):
    return (-math.expm1(-intensity(x,d,strength)))*(-math.expm1(-intensity(x,-d,strength)))

def predicted_maximizers(d, strength):
    q=strength*math.exp(-d)
    if q>=1:
        return (0.0,)
    if q<=d/math.sinh(d):
        return (-d,d)
    lo,hi=0.0,d
    for _ in range(70):
        md=(lo+hi)/2
        if md/math.sinh(md)>q:
            lo=md
        else:
            hi=md
    x=(lo+hi)/2
    return (-x,x)

def main():
    checks=0
    d=math.log(4)
    strength=16*math.log(2)/3
    roots=predicted_maximizers(d,strength)
    assert len(roots)==2
    assert all(abs(abs(x)-math.log(2))<3e-14 for x in roots)
    assert abs(mean_served(roots[0],d,strength)-(2-2**(-8/3)-2**(-2/3)))<1e-14
    checks+=3
    rng=random.Random(20261120)
    for _ in range(800):
        d=rng.uniform(0.07,6)
        q=rng.uniform(0.01,2.5)
        strength=q*math.exp(d)
        cand=predicted_maximizers(d,strength)
        best=mean_served(cand[0],d,strength)
        assert all(abs(mean_served(x,d,strength)-best)<3e-13 for x in cand)
        checks+=1
        for j in range(301):
            x=-d*1.5+3*d*j/300
            assert mean_served(x,d,strength)<=best+4e-12
            assert both_served(x,d,strength)<=both_served(0,d,strength)+5e-13
            checks+=2
    # Fixed strength > 1 crosses center, interior, endpoint as separation increases.
    for strength in (1.01,1.2,2,5,20):
        d1=math.log(strength)
        def edge_threshold(d):
            return 2*d/(-math.expm1(-2*d))
        lo,hi=d1, max(d1,2.0)
        while edge_threshold(hi)<strength:hi*=2
        for _ in range(75):
            md=(lo+hi)/2
            if edge_threshold(md)<strength:lo=md
            else:hi=md
        d2=(lo+hi)/2
        assert d2>d1
        assert len(predicted_maximizers(d1/2,strength))==1
        assert len(predicted_maximizers((d1+d2)/2,strength))==2
        assert len(predicted_maximizers(d2+1,strength))==2
        assert abs(abs(predicted_maximizers(d2+1,strength)[0])-(d2+1))<1e-12
        checks+=5
    print('PASS:',checks,'supplementary assertions; general claim rests on analytic proof')

if __name__=='__main__':main()
